class str2Doc(object):
    def __init__(self, keyStr, separator=","):
        self.separator= separator
        self.keys= keyStr.split(separator)
    def convert (self, line):
        values= line.split(self.separator)
        if len(values) == len(self.keys):
            d= {}
            i=0 
            while i < len(values):
                key= self.keys[i]
                val= values[i]
                d[key]= val
                i= i+1
            return d 


