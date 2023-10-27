#----- UTILITY FUNCTIONS ----- #
#convert byte to string
def byte_to_string(byte):
    return str(bytes(byte))[1:][1:-1]

#convert list to single string
def list_to_string(LIST):
    STRING = ""
    for data in LIST:
        STRING+=str(data)
        if LIST.index(data)==len(LIST)-1:
            STRING+=';'
        else:
            STRING+=', '
    return STRING

#convert table description to table schema
def desc_to_schema(desc):
    schema = "("
    for row in desc:
        schema+=str(row[0])+" "+str(byte_to_string(row[1]))
        if desc.index(row)==len(desc)-1:
            schema+=')'
        else:
            schema+=', '
    return schema

#----- CONNECTING TO THE DATABASE ------#
import mysql.connector as mysql
import getpass
def make_connection():
    host = input("host: ")
    user = input("user: ")
    port = int(input("port: "))
    password = getpass.getpass("password: ")
    config = {
                "host":host,
                "user":user,
                "port":port,
                "password":password    
            }
    
    other = int(input("how many additional configs? (0 for none)"))
    for i in range(other):
        key = input("enter the config name: ")
        value = input("enter the config value: ")
        config[key] = value
    try:
        conn = mysql.connect(**config)
        return conn
    except Exception as e:
        print(e)
        print("the connection couldn't be establised")
        exit()
conn = make_connection()
#----- MAIN PART OF THE PROGRAM -------#
command_file = open("commands.txt","w")

cursorObj = conn.cursor()

#getting the table names in current database
cursorObj.execute("SHOW TABLES")
tables = cursorObj.fetchall()

#storing the name,creation, insertion command in the file
for table in tables:
    #GET THE TABLE NAME
    tb_name = byte_to_string(table[0])

    #the comment for the table name
    command_file.write(f"/*THE {tb_name} TABLE*/\n")
    
    #GET THE TABLE SCHEMA 
    cursorObj.execute("DESCRIBE "+tb_name)
    description = cursorObj.fetchall()
    tb_schema = desc_to_schema(description)

    #the creation command
    command_file.write(f"CREATE TABLE {tb_name} "+tb_schema+';\n')
    
    #GET THE TABLE DATA AND CREATE INSERTION COMMANDS
    cursorObj.execute("SELECT * FROM "+tb_name)
    content = list_to_string(cursorObj.fetchall())
    
    #the insertion command
    command_file.write(f"INSERT INTO {tb_name} VALUES "+content+'\n\n')

#---- CLOSING THE CONNECTION,CURSOR AND FILE ----#
command_file.close()
cursorObj.close()
conn.close()
