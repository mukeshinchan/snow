from flask import Flask,render_template
import snowflake.connector as ct

app=Flask(__name__,template_folder='template')
@app.route('/')
def home():
    ctx=ct.connect(
    user='MUKESHKANNAN4',
    password='*15219633#Mc',
    account='mb23720.ca-central-1.aws')
    cs= ctx.cursor()
    try:
        #cs.execute("SELECT current_version()")
        #ne_row = cs.fetchall()
        #cs.execute('CREATE WAREHOUSE IF NOT EXISTS FIRST')
        #cs.execute('CREATE DATABASE IF NOT EXISTS FIRST_DB')  
        #cs.execute('CREATE SCHEMA IF NOT EXISTS FIRST_SCHEMA')
        #cs.execute('CREATE TABLE table_1 (plant_name varchar(50), UOM varchar(50), Low_End_of_Range int , High_End_of_Range int )')
        #database=input('Data base :')
        cs.execute(f'USE DATABASE FIRST_DB')
        #table=input('Table :')
        cs.execute(f"SELECT * FROM flask ")
        df=cs.fetchall()
    finally:
        cs.close()
        ctx.close()
    return render_template('home.html',data_1=df)



if (__name__=='__main__'):
    app.run(debug=True)
