from flask import Flask, render_template
import os
from acitoolkit.acitoolkit import Session, Tenant
from acitoolkit.aciHealthScore import HealthScore
import json


# initialize ACI toolkit session
APIC_URL = os.getenv("APIC_URL")
APIC_LOGIN = os.getenv("APIC_LOGIN")
APIC_PASSWORD = os.getenv("APIC_PASSWORD")
SESSION = Session(APIC_URL, APIC_LOGIN, APIC_PASSWORD)
SESSION.login()

# Eliminate Trailing slash
if APIC_URL.endswith('/'):
    APIC_URL = APIC_URL[:-1]


app = Flask(__name__)

def get_tenants():
    """
    return a list of ACIToolkit tenant objects
    """
    # your code goes here
    pass


def get_tenant_healthscore(obj):
    """
    Returns a healthscore for a particular tenants

    :param obj: acitoolkit Tenant object
    :return: current health score
    """

    # your code replaces the following line
    return 100



def get_tenant_faultcounts(obj):
    """
    return fault counts for a tenant
    """
    # your code replaces the following line
    pass

@app.route('/')
def react():
    # This view doesn't actually send any data to the template, the client
    #will retrieve it via API calls (and eventually websockets)
    return render_template('react.html')

@app.route('/api/tenants')
def dash():
    """
    API which returns tenant list with additional information we've created
    """

    data = list()

    tenants = get_tenants()

    for t in tenants:

        score = get_tenant_healthscore(t)

        i = {"name": t.name,
             "dn": t.dn,
             "score": score,
             }

        data.append(i)
    return json.dumps(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
