#!/usr/bin/python3 -B

# Copyright 2023 mjbots Robotic Systems, LLC.  info@mjbots.com
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


"""
This example commands a single servo at ID #1 using the default
transport to hold the current position indefinitely, and prints the
state of the servo to the console.
"""

import asyncio
import math
import moteus

async def main():
    # By default, Controller connects to id 1, and picks an arbitrary
    # CAN-FD transport, prefering an attached fdcanusb if available.
    c = moteus.Controller(id = 1)
    s = moteus.Stream(c)
    
    results = await c.set_position(position=-1.0, velocity= 0.0, velocity_limit=2.0, accel_limit=10.0, query=True)
    print(results)
    
    await asyncio.sleep(3.0)
    
    results = await c.set_position(position=1.0, velocity= 0.0, velocity_limit=2.0, accel_limit=10.0, query=True)
    print(results)
    
    await asyncio.sleep(3.0)
    
    results = await c.query()
    print(results)
    
    await asyncio.sleep(3.0)
    
    await c.set_stop()
    
    results = await c.query()
    print(results)

    
if __name__ == '__main__':
    asyncio.run(main())


