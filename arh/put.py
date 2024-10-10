import etcd3


if __name__ == "__main__":
    client = etcd3.client()
    client.put("start-requested", "now")
    print('Key "start-requested" set to "now"')
