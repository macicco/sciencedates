#!/usr/bin/env python
import datetime
from pytz import timezone, UTC
from numpy.testing import assert_allclose,assert_equal
import unittest
#
import sciencedates as sd

class BasicTest(unittest.TestCase):
    def test_yearint(self):
        t0 = datetime.datetime(2013,7,2,12,0,0,tzinfo=UTC)
        yd,utsec = sd.datetime2yd(t0)

        utsec2 = sd.dt2utsec(t0)

        assert sd.yd2datetime(yd,utsec) == t0
        assert utsec==utsec2

    def test_yeardec(self):
        adatetime = datetime.datetime(2013,7,2,12,0,0,tzinfo=UTC)
        yeardec = sd.datetime2yeardec(adatetime)

        assert_allclose(yeardec,2013.5)
        assert sd.yeardec2datetime(yeardec) == adatetime

    def test_utc(self):
        t0 = datetime.datetime(2013,7,2,12,0,0)
        estdt = timezone('EST').localize(t0)
        utcdt = sd.forceutc(estdt)

        assert utcdt==estdt
        assert utcdt.tzname()=='UTC'


        d0 = datetime.date(2013,7,2)
        assert sd.forceutc(d0) == d0

    def test_gtd(self):
        adatetime = datetime.datetime(2013,7,2,12,0,0)
        iyd,utsec,stl= sd.datetime2gtd(adatetime,glon=42)

        assert iyd[0]==183
        assert_allclose(utsec[0],43200)
        assert_allclose(stl[0],14.8)


    def test_findnearest(self):
        indf,xf = sd.find_nearest([10,15,12,20,14,33],[32,12.01])
        assert_allclose(indf,[5,2])
        assert_allclose(xf,[33.,12.])

        indf,xf = sd.find_nearest((datetime.datetime(2012,1,1,12),
                                   datetime.datetime(2012,1,1,11)),
                                   datetime.datetime(2012,1,1,11,30))
        assert_equal(indf,0)
        assert_equal(xf, datetime.datetime(2012,1,1,12))

    def test_randomdate(self):
        assert sd.randomdate(2018).year == 2018


if __name__ == '__main__':
    unittest.main()
