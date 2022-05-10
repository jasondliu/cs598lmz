import select  # 注意这个select
import sys

__doc__ = """
    一个时区转换器，用于将一个时区与另一个时区进行时间转换
"""

I_WANT_TO_EXIT = False


class ZoneChanger:
    def __init__(self):
        self.cities = ['Sydney', 'Melbourne', 'Gold coast', 'Perth',
                       'Adelaide', 'Brisbane', 'Darwin', 'Hobart',
                       'Alice spring', 'Cairns', 'Canberra']
        self.timezones = [datetime.timezone(datetime.timedelta(hours=10)),
                          datetime.timezone(datetime.timedelta(hours=+9.5)),
                          datetime.timezone(datetime.timedelta(hours=10)),
                          datetime.timezone(datetime.timedelta
