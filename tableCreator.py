#utility to convert byte to string
def byte_to_string(byte):
    return str(bytes(byte))[1:][1:-1]

#connecting to the database
import mysql.connector as mysql
config = {
    "host":"172.30.171.41",
    "user":"client",
    "password":"chaitra",
    "port":3306,
    "auth_plugin":"mysql_native_password","database":"mock"
}


try:
    conn = mysql.connect(**config)
except Exception as e:
    print(e)
    print("the connection couldn't be establised")
    exit()
cursorObj = conn.cursor()

cursorObj.execute("SHOW TABLES")
tables = cursorObj.fetchall()
commands = []
command_file = open("insertion_commands.txt","w")
def list_to_string(LIST):
    STRING = ""
    for data in LIST:
        STRING+=str(data)
    return STRING
for table in tables:
    tb_name = byte_to_string(table[0])
    cursorObj.execute("SELECT * FROM "+tb_name)
    content = list_to_string(cursorObj.fetchall())

    commands.append(f"INSERT INTO {tb_name} VALUES "+content+';\n')

for command in commands:
    command_file.write(command)
command_file.close()
cursorObj.close()
conn.close()