import psycopg2


def query(query: str):
    try:
        conn = psycopg2.connect(database='test', 
                            user='postgres', 
                            password='G89811325f', 
                            host='localhost', 
                            port='5432')
        cursor = conn.cursor()


        if query.split(" ")[0] == "INSERT":
            try:
                cursor.execute(query)
                conn.commit()
                return {"Succesfully created data"}


            except Exception as e:
                print(e)
                return {"Error"}
      

        elif query.split(" ")[0] == "SELECT":
           try:
                cursor.execute(query)
                data = cursor.fetchall()


                if data:
                    return data[0]
                
                
                return False
            

            except Exception as e: 
                print(e)
                return {"Error"}


        elif query.split(" ")[0] == "SELECT" and type == "all":


            try:
                cursor.execute(query)
                data = cursor.fetchall()


                if data:
                    return data[0]
                
                
                return False
            

            except Exception as e: 
                print(e)
                return {"Error"}
              
              
        elif query.split(" ")[0] == "SELECT" and type == "one":
            try:
                cursor.execute(query)
                return  cursor.fetchone()

              
            except Exception as e:
                print(e)
                return {"Error"}
        

        elif query.split(" ")[0] == "UPDATE":
                print(data)
            
            
                if data:
                    return data
                
                
                return {404}
              
              
            except Exception as e:
                print(e)
                return {"Error"}


        elif query.split(" ")[0] == "UPDATE":
            try:
                cursor.execute(query)
                conn.commit()
                return {"Succesfully updated data"}


            except Exception as e:
                print(e)
                return {"Error"}
            

        elif query.split(" ")[0] == "DELETE":
            try:
                cursor.execute(query)
                conn.commit()
                return {"Successfully deleted data"}


            except Exception as e:
                print(e)
                return {"Error"}

              
        else:
            return {"Bad query"}


    except psycopg2.OperationalError as e:
        return {"Can\'t establish connection to database. Error:": e}


    finally:
        cursor.close()
        conn.close()