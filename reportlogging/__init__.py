# -*- coding:utf-8 -*-
import logging
logger = logging.getLogger(__name__)


class MultiLogger(object):
    def __init__(self, loggers=None):
        self.loggers = loggers or []

    def apply_all(self, name, *args, **kwargs):
        for logger in self.loggers:
            try:
                getattr(logger, name)(*args, **kwargs)
            except AttributeError:
                raise
            except Exception as e:
                logger.warn("exception is raised %s", e, exc_info=True)

    def debug(self, msg, *args, **kwargs):
        return self.apply_all("debug", msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        return self.apply_all("info", msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        return self.apply_all("warning", msg, *args, **kwargs)

    def warn(self, msg, *args, **kwargs):
        return self.apply_all("warn", msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        return self.apply_all("error", msg, *args, **kwargs)

    def exception(self, msg, *args, **kwargs):
        return self.apply_all("exception", msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        return self.apply_all("critical", msg, *args, **kwargs)

    def fatal(self, msg, *args, **kwargs):
        return self.apply_all("fatal", msg, *args, **kwargs)

    def log(self, level, msg, *args, **kwargs):
        return self.apply_all("log", level, msg, *args, **kwargs)
