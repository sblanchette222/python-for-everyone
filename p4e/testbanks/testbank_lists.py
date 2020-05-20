"""
This is a testbank of questions that use lists.

Use this on the final.
"""

import random
from p4e import testlib 

class T03ListFilter(testlib.TestCase):
    """
    Write a function called ``list_filter()`` that takes two arguments, ``number_list`` 
    and ``limit``. ``number_list`` is a list of floats and ``limit`` is a float. 
    The function returns a list containing only the numbers in ``number_list`` that are less than or equal to ``limit``.

    - Arguments:
        - ``number_list`` - A list of floats
        - ``limit``- Return numbers in ``number_list`` that are less than or equal to this. 
    - Returns:
        - The numbers in ``number_list`` that are less than or euqal to ``limit``
        
    """

    test_hasattr = 'list_filter'

    @staticmethod
    def solution(number_list, limit):
        """Filter this list."""
        output = []
        for num in number_list:
            if num < limit:
                output.append(num)
        return output

    def test_1_check_list(self):
        """Test list_filter()"""
        nums = []
        for i in range(random.randint(20, 100)):
            nums.append(random.uniform(1, 1000))
        limit = random.uniform(400, 600)
        exp = sorted([x for x in nums if x < limit])
        dut = self.sandbox_function(self.test_hasattr)
        got = sorted(dut(nums, limit))
        self.compare(exp, got)
