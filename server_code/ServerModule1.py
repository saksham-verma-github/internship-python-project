import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
@anvil.server.callable
def submit1(name, prn, address, email, mobile, blood):
    app_tables.personalinfo.add_row(name=name, prn=prn, email=email, mobile=mobile, address=address, blood=blood)

@anvil.server.callable
def submit2(tenth, twelth, cet, jee, sem):
    app_tables.academicinfo.add_row(tenth=tenth, twelth=twelth, cet=cet, jee=jee, sem=sem)

@anvil.server.callable
def submit3(certification, linkedin, experience):
    app_tables.expericeneinfo.add_row(certification=certification, linkedin=linkedin, experience=experience)


@anvil.server.callable
def merge_data():
    # Create a new table to hold the merged data
    merged_table = app_tables.merged_data

    # Retrieve data from the first table (personalinfo)
    for row in app_tables.personalinfo.search():
        merged_table.add_row(name=row['name'], prn=row['prn'], email=row['email'], mobile=row['mobile'], address=row['address'], blood=row['blood'])

    # Retrieve data from the second table (academicinfo)
    for row in app_tables.academicinfo.search():
        merged_table.add_row(tenth=row['tenth'], twelth=row['twelth'], cet=row['cet'], jee=row['jee'], sem=row['sem'])

    # Retrieve data from the third table (experienceinfo)
    for row in app_tables.experienceinfo.search():
        merged_table.add_row(certification=row['certification'], linkedin=row['linkedin'], experience=row['experience'])

    return "Data merged successfully!"