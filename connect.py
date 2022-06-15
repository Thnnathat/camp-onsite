import mysql.connector

class Connect:
    def __init__(self):
        pass
    def conn(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="thunder",
                password="0980620014",
                database="hardware"
            )
            return mydb
        except mysql.connector.Error as err:
            print(err)
            print("Error at connect.")
            
            
class Manager(Connect):
    def __inti__(self):
        pass

    def select_all(self, table_name):
        try:
            mydb = self.conn()
            cs = mydb.cursor(dictionary=True)
            sql = f"SELECT * FROM {table_name}"
            cs.execute(sql)
            data = cs.fetchall()
            cs.close()
            mydb.close()
            return data
        except:
            print("Error at select.")

    def select_name_only(self, *args, table_name):
        try:
            key = ",".join(args)
            mydb = self.conn()
            cs = mydb.cursor(dictionary=True)
            sql = f"SELECT {key} FROM {table_name}" 
            cs.execute(sql)
            data = cs.fetchall()
            cs.close()
            mydb.close()
            return data
        except Exception as err:
            print("Error at select name only.")
            data = err
            return data

    def insert(self, *args, table_name):
        try:
            mydb = self.conn()
            cs = mydb.cursor()
            sql = f"INSERT INTO {table_name} VALUES {args}"
            cs.execute(sql)
            mydb.commit()
            cs.close()
            mydb.close()
            return True
        except:
            return False
        
    def update(self, status, value, Id, table_name):
        try:
            mydb = self.conn()
            cs = mydb.cursor()
            sql = f"UPDATE {table_name} SET status = '{status}', value = {value} WHERE Id = {Id}"
            cs.execute(sql)
            mydb.commit()
            cs.close()
            mydb.close()
            return True
        except Exception as err:
            print("Error at update: ",err)
            return False 

    def delete(self, Id, table_name):
        try:
            mydb = self.conn()
            cs = mydb.cursor()
            sql = f"DELETE FROM {table_name} WHERE Id = {Id}"
            cs.execute(sql)
            mydb.commit()
            cs.close()
            mydb.close()
            return True
        except mysql.connector.Error as err:
            print(err)
            return False

    def select_waere_min_id(self):
        mydb = self.conn()
        cs = mydb.cursor()
        sql = "SELECT * FROM hardware_control WHERE Id = (SELECT MIN(Id) FROM hardware_control)"
        cs.execute(sql)
        data = cs.fetchall()
        cs.close()
        mydb.close()
        return data
        
if __name__ == "__main__":
    pass
    database = Manager()
    # data = database.select_all(table_name="hardware_control")
    # data2 = database.select_name_only("name", "kind", table_name="hardware_control")
    # data3 = database.insert(0, "A1", "fan", "on", 1, table_name="hardware_control")
    # data4 = database.update(status="off", value=0, Id=8, table_name="hardware_control")
    # data5 = database.delete(Id=7, table_name="hardware_control")
    # data6 = database.update2(Id='0', name="fan", kind="fan",status="on", value='1')
    # data7 = database.select_waere_min_id()
    # print(data5)
    # print(data7)
  