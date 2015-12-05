# -*- coding:utf-8 -*-
import unittest


class Tests(unittest.TestCase):
    def _getTargetClass(self):
        from reportlogging import ReportLoggerManager
        return ReportLoggerManager

    def _makeOne(self):
        return self._getTargetClass()()

    def test_non_activate__not_captured(self):
        target = self._makeOne()
        target.logger.info("foo")
        result = target.getvalue()
        self.assertEqual(result, "")

    def test_activate__captured(self):
        target = self._makeOne()
        target.activate()
        target.logger.info("foo")
        result = target.getvalue()
        self.assertNotEqual(result, "")

    def test_activate__preactivate_message_is_not_captured(self):
        target = self._makeOne()
        target.logger.info("foo")
        target.activate()
        result = target.getvalue()
        self.assertEqual(result, "")
