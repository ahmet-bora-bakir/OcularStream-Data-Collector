import json

screenRes_x_MAX = 1920
screenRes_y_MAX = 1080
screenRes_x = []
screenRes_y = []

screenRes_x.append(0)
screenRes_x.append(1920)
screenRes_y.append(0)
screenRes_y.append(1080)

class EyeTracker:
    def __init__(self):
        self.category = "null"
        self.tracker = "null"
        self.request = "null"
        self.statuscode = 0


        self.avg_x = []
        self.avg_y = []

        self.leftEye_avg_x = []
        self.leftEye_avg_y = []

        self.leftEye_pcenter_x = []
        self.leftEye_pcenter_y = []

        self.leftEye_psize = []

        self.leftEye_raw_x = []
        self.leftEye_raw_y = []

        self.raw_x = []
        self.raw_y = []

        self.rightEye_avg_x = []
        self.rightEye_avg_y = []

        self.rightEye_pcenter_x = []
        self.rightEye_pcenter_y = []
    
        self.rightEye_psize = []

        self.rightEye_raw_x = []
        self.rightEye_raw_y = []

        self.time = []
        self.timestamp = []

    def equal(self, other, index):

        other.avg_x.append(self.avg_x[index])
        other.avg_y.append(self.avg_y[index])

        other.leftEye_avg_x.append(self.leftEye_avg_x[index])
        other.leftEye_avg_y.append(self.leftEye_avg_y[index])

        other.leftEye_pcenter_x.append(self.leftEye_pcenter_x[index])
        other.leftEye_pcenter_y.append(self.leftEye_pcenter_y[index])

        other.leftEye_psize.append(self.leftEye_psize[index])

        other.leftEye_raw_x.append(self.leftEye_raw_x[index])
        other.leftEye_raw_y.append(self.leftEye_raw_y[index])
    
        other.raw_x.append(self.raw_x[index])
        other.raw_y.append(self.raw_y[index])
    
        other.rightEye_avg_x.append(self.rightEye_avg_x[index])
        other.rightEye_avg_y.append(self.rightEye_avg_y[index])
                                    
        other.rightEye_pcenter_x.append(self.rightEye_pcenter_x[index])
        other.rightEye_pcenter_y.append(self.rightEye_pcenter_y[index])
                                        
        other.rightEye_psize.append(self.rightEye_psize[index])

        other.rightEye_raw_x.append(self.rightEye_raw_x[index])
        other.rightEye_raw_y.append(self.rightEye_raw_y[index])

        other.time.append(self.time[index])
        other.timestamp.append(self.timestamp[index])

    def range_time(self, boundedData, unintendedData):
        while(True):
            try:
                time_input = int(input("Please input time(milliseconds): "))
                if(time_input < 0):
                    raise ValueError("Out of range!")
                break
            
            except(ValueError):
                print("Invalid input! Please input numbers within range(time > 0).")
        for i in range(len(self.time)):
            if(self.time[i] > time_input):
                self.equal(unintendedData, i)
            else:
                self.equal(boundedData, i)
    def show_time(self):
        while(True):
            try:
                timeType = input("Please enter time type(\"milliseconds\" or \"timestamp\"): ")
                if(timeType != "milliseconds" or timeType != "timestamp"):
                    raise NameError()
                time_n = int(input("Please enter how many time datas you want to see(ex: first 10 time in milliseconds): "))
                if(time_n < 0):
                    raise ValueError("Out of range!")
                break
            except(ValueError):
                print("Invalid input! Please input numbers within range(time_n > 0).")
            except(NameError):
                print("Time type is undefined.")

        if(timeType == "milliseconds"):
            print("Time datas for eye tracker(in milliseconds): ")
            for x in range(time_n):
                print(self.time[x], end= " ")
        else:
            print("Time datas for eye tracker(in time stamp): ")
            for x in range(time_n):
                print(self.timestamp[x])
            

    def shift_time(self):
        while(True):
            timeShift = float(input("Please input time(milliseconds): "))
            for x in range(self.time):
                self.time[x] += timeShift

            decision = input("See time data y/Y else otherwise: ")
            while(True):
                if(decision == 'Y' or decision == 'y'):
                    self.show_time
                else:
                    break

            continue_ = input("Enter c/C to continue else otherwise: ")
            if(continue_ != 'C' or continue_ != 'c'):
                break

class DeviceTime:
    def __init__(self):
        time = []
    
    def time_sync(self, other):
        




while(True):
    try:
        fileName = input("Filename (without .txt): ") + ".txt"
        with open(fileName, 'r') as file:
            print(f"File '{fileName}' found and opened successfully!")
            break
    except FileNotFoundError:
        print(f"Error: '{fileName}' not found!")
        user_choice = input("Type 'exit' to quit or press any key to try again: ")
        if user_choice.lower() == "exit":
            exit(0)

rawData = EyeTracker()
boundedData = []
unintendedData = []
eyeTracker_dataIndex = 0

with open(fileName, "r") as file:
    for line in file:
        try:
            data = json.loads(line)
            # data["values"]["frame"]["avg"]["x"]
            frame = data["values"]["frame"]
            
            rawData.avg_x.append(frame["avg"]["x"])
            rawData.avg_y.append(frame["avg"]["y"])

            rawData.leftEye_avg_x.append(frame["lefteye"]["avg"]["x"])
            rawData.leftEye_avg_y.append(frame["lefteye"]["avg"]["y"])

            rawData.leftEye_pcenter_x.append(frame["lefteye"]["pcenter"]["x"])
            rawData.leftEye_pcenter_y.append(frame["lefteye"]["pcenter"]["y"])

            rawData.leftEye_psize.append(frame["lefteye"]["psize"])

            rawData.leftEye_raw_x.append(frame["lefteye"]["raw"]["x"])
            rawData.leftEye_raw_y.append(frame["lefteye"]["raw"]["y"])
            
            rawData.raw_x.append(frame["raw"]["x"])
            rawData.raw_y.append(frame["raw"]["y"])
            
            rawData.rightEye_avg_x.append(frame["righteye"]["avg"]["x"])
            rawData.rightEye_avg_y.append(frame["righteye"]["avg"]["y"])

            rawData.rightEye_pcenter_x.append(frame["righteye"]["pcenter"]["x"])
            rawData.rightEye_pcenter_y.append(frame["righteye"]["pcenter"]["y"])

            rawData.rightEye_psize.append(frame["righteye"]["psize"])

            rawData.rightEye_raw_x.append(frame["righteye"]["raw"]["x"])
            rawData.rightEye_raw_y.append(frame["righteye"]["raw"]["y"])

            rawData.time.append(frame["time"])
            rawData.timestamp.append(frame["timestamp"])
            
        except (json.JSONDecodeError, KeyError):
            continue
