# -*- coding:utf-8 -*-
import logging
from reportlogging import manager
logger = logging.getLogger(__name__)
report_logger = manager.getLogger(logger)


def batch():
    report_logger.info("starting batch ...")
    print("...")
    report_logger.info("ending batch ...")


def main():
    from reportlogging import manager
    manager.activate()
    batch()
    print("output:{}".format(manager.getvalue()))


if __name__ == "__main__":
    main()
