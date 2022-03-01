#!/usr/bin/python
# -*- coding: utf-8 -*-

import string
import random

# printing letters
letters = string.ascii_letters
print(''.join(random.choice(letters) for i in range(10)))
