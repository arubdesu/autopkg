#!/usr/local/autopkg/python
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import imp
import os
import unittest
from unittest.mock import patch

import autopkglib.common

autopkg = imp.load_source(
    "autopkg", os.path.join(os.path.dirname(__file__), "..", "autopkg")
)


class TestCommon(unittest.TestCase):
    """Test class for common"""

    def setUp(self):
        ## TODO - when we do leverage globalPreferences, it gets imported with
        # from autopkglib.prefs import Preferences
        ## and then
        # globalPreferences = Preferences() as per https://github.com/autopkg/autopkg/blob/f2c9b5beb42052fe9f291c5bba7a0381642c36cf/Code/autopkglib/__init__.py#L95C1-L95C34
        pass

    def tearDown(self):
        pass

    @patch("autopkglib.common.sys")
    def test_is_mac_returns_true_on_mac(self, mock_sys):
        """On macOS, is_mac() should return True."""
        mock_sys.platform = "Darwin-somethingsomething"
        result = autopkglib.common.is_mac()
        self.assertEqual(result, True)

    @patch("autopkglib.common.sys")
    def test_is_mac_returns_false_on_not_mac(self, mock_sys):
        """On not-macOS, is_mac() should return False."""
        mock_sys.platform = "Win32-somethingsomething"
        result = autopkglib.common.is_mac()
        self.assertEqual(result, False)

    @patch("autopkglib.common.sys")
    def test_is_windows_returns_true_on_windows(self, mock_sys):
        """On Windows, is_windows() should return True."""
        mock_sys.platform = "Win32-somethingsomething"
        result = autopkglib.common.is_windows()
        self.assertEqual(result, True)

    @patch("autopkglib.common.sys")
    def test_is_windows_returns_false_on_not_windows(self, mock_sys):
        """On not-Windows, is_windows() should return False."""
        mock_sys.platform = "Darwin-somethingsomething"
        result = autopkglib.common.is_windows()
        self.assertEqual(result, False)

    @patch("autopkglib.common.sys")
    def test_is_linux_returns_true_on_linux(self, mock_sys):
        """On Linux, is_linux() should return True."""
        mock_sys.platform = "Linux-somethingsomething"
        result = autopkglib.common.is_linux()
        self.assertEqual(result, True)

    @patch("autopkglib.common.sys")
    def test_is_linux_returns_false_on_not_linux(self, mock_sys):
        """On not-Linux, is_linux() should return False."""
        mock_sys.platform = "Win32-somethingsomething"
        result = autopkglib.common.is_linux()
        self.assertEqual(result, False)

    def test_get_autopkg_version(self):
        """Asserts get_autopkg_version() returns a version in the expected format.
           Allows 2.0, 2.0.1, but not 2.0. or other funky-formatted versions.
           (Confirmed there's never been another style by hitting the 'history' button
           while viewing blame for Code/autopkglib/version.plist's Version value)
        """
        result = autopkglib.common.get_autopkg_version()
        self.assertRegex(result, r'\d+\.\d+(\.\d+)?')
