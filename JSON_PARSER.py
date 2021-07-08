import json

class JSONParser(object):

    def __init__(self, json_file):
        self.json_file = json_file
        self.data = {}

    def parse_dict_or_list(self, key, d):
        if isinstance(d, list):
            for sub_dict in d:
                if key in sub_dict:
                    return sub_dict[key]
            return None
        else:
            if key in d:
                return d[key]
            else:
                None

    def make_query(self, query_list):
        working_level = self.data
        for item in query_list:
            working_level = self.parse_dict_or_list(item, working_level)
            if working_level == None:
                return None
        return working_level

    def load_json(self):
        with open(self.json_file) as data_file:
            self.data = json.load(data_file)

    def query(self, query_string):
        self.load_json()
        result = self.make_query(query_string.split('/'))
        return result


p = JSONParser('userdata.json')
result = p.query('ABC/DEF/OverAllHealth/CPUs/Status/MemorySummary/TotalSystemMemoryGiB')
print(result)
result = p.query("ABC/DEF/OverAllHealth/PowerSupplies/Status")
print(result)
