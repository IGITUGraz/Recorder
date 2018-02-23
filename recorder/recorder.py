class Recorder:
    def __init__(self, *datastores):
        self.datastores = datastores
        for datastore in self.datastores:
            datastore.connect()

    def record(self, key, val):
        for datastore in self.datastores:
            if not datastore.get(key):
                datastore.initarr(key)
            datastore.append(key, val)

    def get(self, key, datastore=None):
        if datastore is not None:
            return datastore.get(key)
        else:
            return self.datastores[0].get(key)
