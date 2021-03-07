#!/usr/bin/env python
import snowflake.connector
from decouple import config

USERNAME = config('USER')
USERPASSWORD = config('PASSWORD')
USERACCOUNT = config('ACCOUNT')
print("user name:"+ USERNAME)
print("password=" + USERPASSWORD)
# Gets the version
ctx = snowflake.connector.connect(
    user = USERNAME,
    password = USERPASSWORD,
    account= USERACCOUNT
    )
cs = ctx.cursor()
try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print(one_row[0])
finally:
    cs.close()
ctx.close()