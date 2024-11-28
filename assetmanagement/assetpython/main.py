from vendor import vendor
from software import software
from device import device
from employee import employee
from installation import installation

from datetime import datetime

class assetmanagement:
    def __init__(self):
        self.vendorlist=[]
        self.softwarelist=[]
        self.employeelist=[]
        self.devicelist=[]
        self.installedsoftwares=[]
        
    def noofinstallation(self,softwarename):
        count=0
        for softwares in self.installedsoftwares:
            if softwares.softwarename==softwarename:
                count+=1
        return count
    
    def noofsoftwaresondevice(self,did):
        count=0
        for softwares in self.installedsoftwares:
            print(softwares.deviceid)
            if softwares.deviceid==did:
                count+=1
        return count
    
    def noofsoftwareforemployee(self,eid):
    
        did=self.getdeviceid(eid)
        count=0
        for i in did:
            count+= self.noofsoftwaresondevice(i)
        return count
        
    def getdeviceid(self,eid):
        deviceidlist=[]
        for device in self.devicelist:
            if device.employeeid==eid:
                deviceidlist.append( device.deviceid)
        return deviceidlist
            
    def amountonsoftware(self,softwarename):
        cnt=self.noofinstallation(softwarename)
        amount=self.getamount(softwarename)
        return cnt*amount
        
    def getamount(self,softwarename):
        for softwares in self.softwarelist:
            if softwares.softwarename==softwarename:
                return softwares.cpd
            else:
                return 0
            
    def amountonemployee(self,eid):
        amount=0
        did=self.getdeviceid(eid)
        for i in did:
            for softwares in self.installedsoftwares:
                if softwares.deviceid==i:
                    sname=softwares.softwarename
                    amount+=self.getamount(sname)
        return amount
    
    def noofinstallationofvendor(self,vid):
        numofinstall=0
        sname=self.softwarenamefromvendor(vid)
        for i in sname:
            numofinstall+=self.noofinstallation(i)
        return numofinstall
        
    def softwarenamefromvendor(self,vid):
        snamelist=[]
        for softwares in self.softwarelist:
            if softwares.vendorid ==vid:
                sname=softwares.softwarename
                snamelist.append(sname)
        return snamelist
    
    def addsoftware(self,software):
        found=False
        for vendor in self.vendorlist:
            if vendor.vendorid== software.vendorid:
                # employee.devicelists.append(devices)
                asset.softwarelist.append(software)
                found=True
                
        if not found:
            print("No vendors")
            return
        else:
            print("software added successfully")
            
    def adddevice(self,devices):
        found=False
        
        for employee in self.employeelist:
            print(employee.employeeid)
            if employee.employeeid == devices.employeeid:
                employee.devicelists.append(devices)
                asset.devicelist.append(devices)
                found=True
                
        if not found:
            print("No employee")
            return
        else:
            print("device added successfully")
            
    
    def expiredsoftware(self,expiredate):
        for softwares in self.installedsoftwares:
            sname=softwares.softwarename
            for s in self.softwarelist:
                if s.softwarename==sname and s.expirydate < expiredate:
                    print(sname)
    
    def addinstall(self,instal):
        devicefound=False
        softwarefound=False
        for device in self.devicelist:
            if device.deviceid==instal.deviceid:
                devicefound=True
                
        for software in self.softwarelist:
            if software.softwarename==instal.softwarename:
                softwarefound=True
                
        if not devicefound:
            print("no device found")
            return
        if not softwarefound:
            print("no software found")
            return
        if deviceid and softwarefound:
            asset.installedsoftwares.append(installations)
            print("software added successfully")
        
            
                    
        

asset=assetmanagement()
while True:
    print("1. Add vendor \n 2. Add software \n 3. Add employee \n 4. Add device \n 5. Install software on device \n 6. generate report \n 7. exit")
    choice=int(input("enter the choice: "))
    match(choice):
        case 1:
            vendorid=input("enter the vendor id: ")
            vendorname=input("enter the vendor name: ")
            vendors=vendor(vendorid,vendorname)
            
            asset.vendorlist.append(vendors)
            print("vendor added successfully")
            
        case 2:
            softwarename=input("enter the software name: ")
            vendorid=input("enter the vendor id: ")
            costperdevice=int(input("enter the cost per device: "))
            date=input("enter the expiry date(yyyy-mm-dd): ")
            expirydate=datetime.strptime(date,"%Y-%m-%d")
            softwares=software(softwarename,vendorid,costperdevice,expirydate)
            
            asset.addsoftware(softwares)
       
            
            
        case 3:
            employeeid=input("enter the emoloyee id: ")
            employeename=input("enter the employee name: ")
            employees=employee(employeeid,employeename)
            
            asset.employeelist.append(employees)
            print("emoloyee added successfully")
            
            
        case 4:
            deviceid=input("enter the device id: ")
            employeeid=input("enter the emoloyee id: ")
            devices=device(deviceid,employeeid)
            asset.adddevice(devices)
            
            
            
        case 5:
            deviceid=input("enter the device id: ")
            softwarename=input("enter the software name: ")
            date=input("enter the expiry date(yyyy-mm-dd): ")
            installationdate=datetime.strptime(date,"%Y-%m-%d")
            installations=installation(deviceid,softwarename,installationdate)
            
            asset.addinstall(installations)
            
            
            
        case 6:
            print("Report menu")
            print("1. Number of installations of a particular software")
            print("2. Number of software installed on a device")
            print("3. Number of software installed for an employee")
            print("4. Amount spent on a software")
            print("5. Amount spent for an employee")
            print("6. Number of installations from a vendor")
            print("7. Devices with expired software")
            ch=int(input("Choose a report option: "))
            match(ch):
                case 1:
                    softwarename=input("Enter Software Name: ")
                    noofinstallation=asset.noofinstallation(softwarename)
                    print(f" Number of installations of a particular {softwarename} is {noofinstallation}")
                    
                case 2:
                   deviceid= input("Enter Device ID: ")
                   noofsoftwareondevice=asset.noofsoftwaresondevice(deviceid)
                   print(f" Number of software installed on a device {deviceid} is {noofsoftwareondevice}")
                case 3:
                    employeeid=input("Enter Employee ID: ")
                    noofsoftwareforemployee=asset.noofsoftwareforemployee(employeeid)
                    print(f" Number of software installed on a device {employeeid} is {noofsoftwareforemployee}")
                case 4:
                   softwarename= input("Enter Software Name: ")
                   amount=asset.amountonsoftware(softwarename)
                   print(f" Amount spent on a software {softwarename} is {amount}")
                   
                case 5:
                   employeeid= input("Enter Employee ID: ")
                   amountonempoyee=asset.amountonemployee(employeeid)
                   print(f" Amount spent on a employee {employeeid} is {amountonempoyee}")
                   
                case 6:
                   vendorid= input("Enter Vendor ID: ")
                   noofinstallationofvendor=asset.noofinstallationofvendor(vendorid)
                   print(f" Number of installations from a vendor {vendorid} is {noofinstallationofvendor}")
                   
                case 7:
                    date=input("enter the expiry date(yyyy-mm-dd): ")
                    installationdate=datetime.strptime(date,"%Y-%m-%d")
                    expiredsoftwares=asset.expiredsoftware(installationdate)
                    
                case __:
                    print("invalid choice")
                    break
            
        case __:
            break
            
            
            
        