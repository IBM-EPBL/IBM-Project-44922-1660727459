import ibm_db


def dbconnect():
    hostname = "21fecfd8-47b7-4937-840d-d791d0218660.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
    uid = "bsk91181"
    pwd = "aCspBg9fQOIeDWfJ"
    driver = "{IBM DB2 ODBC DRIVER}"
    db = "bludb"
    port = "31864"
    cert = "certificate.crt"
    dsn = (
        "DATABASE={0};"
        "HOSTNAME={1};"
        "PORT={2};"
        "UID={3};"
        "SECURITY=SSL;"
        "SSLServerCertificate={4};"
        "PWD={5};"

    ).format(db, hostname, port, uid, cert, pwd)

    try:
        db2 = ibm_db.connect(dsn, "", "")
        print("connected")
        return dsn
    except:

        print("unable to connect", ibm_db.conn_errormsg())
dbconnect()
