# habit.py
from datetime import date, datetime, timedelta

class Habit:
    def __init__(self, name, periodicity, creation_date=None, completion_dates=None):
        """
        Backward-compatible ctor.
        - creation_date is optional -> defaults to today.
        - completion_dates can be ISO strings, datetime, or date objects.
        """
        self.name = name
        self.periodicity = periodicity  # "daily" or "weekly"
        self.creation_date = self._parse_date(creation_date) if creation_date else date.today()
        self.completion_dates = [self._parse_date(d) for d in (completion_dates or [])]

    # ---- Helpers ----
    def _parse_date(self, d):
        """Accept date/datetime/ISO string and return a date."""
        if d is None:
            return None
        if isinstance(d, date) and not isinstance(d, datetime):
            return d
        if isinstance(d, datetime):
            return d.date()
        if isinstance(d, str):
            # Handles 'YYYY-MM-DD' or full ISO 'YYYY-MM-DDTHH:MM:SS[.ffffff]'
            return datetime.fromisoformat(d).date()
        raise ValueError(f"Unsupported date type: {type(d)}")

    def _period_id(self, d: date) -> str:
        """Return a canonical id for the period (day or ISO week)."""
        d = self._parse_date(d)
        if self.periodicity == "daily":
            return d.isoformat()  # e.g., 2025-08-12
        # weekly → ISO week id like 2025-W33
        y, w, _ = d.isocalendar()
        return f"{y}-W{w:02d}"

    def _prev_period(self, d: date) -> date:
        d = self._parse_date(d)
        return d - timedelta(days=1) if self.periodicity == "daily" else d - timedelta(days=7)

    def is_completed_in_period(self, period_date: date) -> bool:
        """True if there is at least one completion in the given period."""
        pid = self._period_id(period_date)
        comp_ids = {self._period_id(x) for x in self.completion_dates}
        return pid in comp_ids

    # ---- Add/alias completion methods ----
    def mark_complete(self, ts: date = None):
        """
        Log a completion for the given timestamp (default: today).
        - Reject future timestamps.
        - Ignore duplicates within the same period (day/week).
        """
        ts = self._parse_date(ts or date.today())
        today = date.today()
        if ts > today:
            raise ValueError("Cannot log a completion in the future.")
        if self.is_completed_in_period(ts):
            return  # ignore duplicate within the same period
        self.completion_dates.append(ts)

    # Backward-compatible alias used by your CLI
    def mark_completed(self):
        self.mark_complete(date.today())

    # ---- Streak logic ----
    def get_streak(self, today: date = None) -> int:
        """
        Count consecutive completed periods ending at the most recent completed
        period (or today if today’s period is completed).
        """
        if not self.completion_dates:
            return 0

        comp_ids = {self._period_id(x) for x in self.completion_dates}
        today = self._parse_date(today or date.today())

        # Start at today's period if completed, otherwise at the last completed period
        start = today if self._period_id(today) in comp_ids else max(self._parse_date(x) for x in self.completion_dates)

        # Count backwards until a gap
        streak = 0
        cursor = start
        while self._period_id(cursor) in comp_ids:
            streak += 1
            cursor = self._prev_period(cursor)

        return streak