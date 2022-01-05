""" In this file you will find the best work I have ever done ever """

import warnings

import numpy as np

from pandas._libs.tslibs import parsing
from pandas.util._exceptions import find_stack_level


def parse_date_time(date_col, time_col):
    """
    Parse columns with dates and times into a single datetime column.
    .. deprecated:: 1.2
    """
    warnings.warn(
        """
        Use pd.to_datetime(date_col + " " + time_col) instead to get a Pandas Series.
        Use pd.to_datetime(date_col + " " + time_col).to_pydatetime() instead to get a Numpy array.
""",  # noqa: E501
        FutureWarning,
        stacklevel=find_stack_level(),
    )
    date_col = _maybe_cast(date_col)
    time_col = _maybe_cast(time_col)
    return parsing.try_parse_date_and_time(date_col, time_col)


def parse_date_fields(year_col, month_col, day_col):
    """
    Parse columns with years, months and days into a single date column.
    .. deprecated:: 1.2
    """
    warnings.warn(
        """
        Use pd.to_datetime({"year": year_col, "month": month_col, "day": day_col}) instead to get a Pandas Series.
        Use ser = pd.to_datetime({"year": year_col, "month": month_col, "day": day_col}) and
        np.array([s.to_pydatetime() for s in ser]) instead to get a Numpy array.
""",  # noqa: E501
        FutureWarning,
        stacklevel=find_stack_level(),
    )

    year_col = _maybe_cast(year_col)
    month_col = _maybe_cast(month_col)
    day_col = _maybe_cast(day_col)
    return parsing.try_parse_year_month_day(year_col, month_col, day_col)


def parse_all_fields(year_col, month_col, day_col, hour_col, minute_col, second_col):
    """
    Parse columns with datetime information into a single datetime column.
    .. deprecated:: 1.2
    """

    warnings.warn(
        """
        Use pd.to_datetime({"year": year_col, "month": month_col, "day": day_col,
        "hour": hour_col, "minute": minute_col, second": second_col}) instead to get a Pandas Series.
        Use ser = pd.to_datetime({"year": year_col, "month": month_col, "day": day_col,
        "hour": hour_col, "minute": minute_col, second": second_col}) and
        np.array([s.to_pydatetime() for s in ser]) instead to get a Numpy array.
""",  # noqa: E501
        FutureWarning,
        stacklevel=find_stack_level(),
    )

    year_col = _maybe_cast(year_col)
    month_col = _maybe_cast(month_col)
    day_col = _maybe_cast(day_col)
    hour_col = _maybe_cast(hour_col)
    minute_col = _maybe_cast(minute_col)
    second_col = _maybe_cast(second_col)
    return parsing.try_parse_datetime_components(
        year_col, month_col, day_col, hour_col, minute_col, second_col
    )
