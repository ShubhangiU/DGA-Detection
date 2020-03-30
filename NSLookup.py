import time

import dns.resolver


def get_records(domain):
    """
    Get all the records associated to domain parameter.
    :param domain: 
    :return: 
    """
    ids = [
        'NONE',
        'A',
        'NS',
        'CNAME',
        'SOA',
        'PTR',
        'MX',
        'TXT',
        'AAAA',
        'LOC',
        'CAA',
    ]

    for a in ids:
        try:
            answers = dns.resolver.query(domain, a)
            for rdata in answers:
                print(a, ':', rdata.to_text())

        except Exception as e:
            print(e)  # or pass

    time.sleep(5)
    print("********************wait for few sec**********************************")



if __name__ == '__main__':
    #with open('C:/Users/upadh/Desktop/d.txt', 'r') as csvFile, open('current.json', 'w') as f:
#filepath = ''
    with open("C:/Users/upadh/Desktop/DGA-Domains.txt") as fp:
        line = fp.readline()
        cnt = 1
        while line:

            line = fp.readline()
           # domain = ("'{}'".format(line.strip()))
            get_records(line.strip())
            #print(domain)
            #get_records('facebook.com')
            cnt += 1



