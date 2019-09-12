# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import unittest

from flaskmessageboard import app


class FlaskMessageBoardTestCase(unittest.TestCase):

    def test_doc(self):
        dev_db = os.path.join(os.path.dirname(app.root_path))
        print(dev_db)


if __name__ == '__main__':
    unittest.main()
