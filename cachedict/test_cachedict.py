# Copyright 2020 Andrew Owen Martin
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
import unittest
import cachedict


class TestCacheDict(unittest.TestCase):
    def test_initialisation_by_dict(self):

        my_cd = cachedict.LRU(
            3,
            {
                num: word
                for num, word in [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
            },
        )

        self.assertTrue(1 not in my_cd)
        self.assertTrue(2 in my_cd)
        self.assertTrue(3 in my_cd)
        self.assertTrue(4 in my_cd)

    def test_initialisation_in_two_steps(self):

        my_cd = cachedict.LRU(maxsize=3)

        my_dict = {
            num: word
            for num, word in [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
        }

        my_cd.update(my_dict)

        self.assertTrue(1 not in my_cd)
        self.assertTrue(2 in my_cd)
        self.assertTrue(3 in my_cd)
        self.assertTrue(4 in my_cd)

    def test_basic(self):

        my_cd = cachedict.LRU(maxsize=3)

        my_cd[1] = "one"
        my_cd[2] = "two"
        my_cd[3] = "three"

        self.assertTrue(1 in my_cd)
        self.assertTrue(2 in my_cd)
        self.assertTrue(3 in my_cd)

        my_cd[4] = "four"

        self.assertTrue(1 not in my_cd)
        self.assertTrue(2 in my_cd)
        self.assertTrue(3 in my_cd)
        self.assertTrue(4 in my_cd)

        my_cd[2]

        self.assertTrue(1 not in my_cd)
        self.assertTrue(2 in my_cd)
        self.assertTrue(3 in my_cd)
        self.assertTrue(4 in my_cd)

        my_cd[5] = "five"

        self.assertTrue(1 not in my_cd)
        self.assertTrue(2 in my_cd)
        self.assertTrue(3 not in my_cd)
        self.assertTrue(4 in my_cd)
        self.assertTrue(5 in my_cd)
