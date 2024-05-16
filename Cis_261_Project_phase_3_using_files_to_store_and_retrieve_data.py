def GetEmpName():
    empname = input("Enter employee name: ")
    return empname

def GetDatesWorked():
    fromdate = input("Enter Start Date (mm/dd/yyy): ")
    todate = input("Enter End Date (mm/dd/yyyy): ")
    return fromdate, todate

def GetHoursWorked():
    hours = float(input("Enter amount of hours worked: "))
    return hours

def GethourlyRate():
    hourlyrate = float(input("enter hourly Rate: "))
    return hourlyrate

def GetTaxRate():
    taxrate = float(input("enter tax rate: "))
    return taxrate

def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(EmpDetailList):
    TotEmployees = 0 
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    
    for EmpList in EmpDetailList:
        fromdate = EmpList[0]
        todate = EmpList[1]
        empname = EmpList[2]
        hours = EmpList[3]
        hourlyrate = EmpList[4]
        taxrate = EmpList[5]
        
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print(fromdate, todate, empname, f"{hours:,.2f}", f"{hourlyrate:,.2f}", f"{grosspay:,.2f}", f"{taxrate:,.1%}", f"{hourlyrate:,.2f}", f"{grosspay:,.2f}", f"{netpay:,.2f}")
                                            
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
         
        EmpTotals["TotEmp"] = TotEmployees
        EmpTotals["TotHrs"] = TotHours
        EmpTotals["TotGrossPay"] = TotGrossPay
        EmpTotals["TotTax"] = TotTax
        EmpTotals["TotNetPay"] = TotNetPay
        
def PrintTotals(EmpTotals):
    print()
    print(f"Total Number of Employees: {EmpTotals['TotEmp']}")
    Print(f"Total Hours Worked: {EmpTotals['TotHrs']}")
    print(f"Total Gross Pay: {EmpTotals['TotGrossPay']}")
    print(f"Total Income Tax: {empTotals['TotTax']:,.2f}")
    print(f"Total Net Pay: {EmpTotals['TotNetPay']:,.2f}")
    
def WriteEmployeeInformation(employee):
    file = open("employeeinfo.txt", "a")
    
file.write('{}|{}|{}|{}|{}|{}\n'.format(employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]))

def GetFromDate():
    valid = False
    from = ""

while not valid:
    
fromdate = input("Enter From Date (mm/dd/yyy): ")

if (len(fromdate.split('/')) != 3 and fromdate.upper() != 'ALL'):
    print("Invalid Date Fromat: ")
    Else:
    valid = True
    Return fromdate
    
def ReadEmployeeInformation(fromdate):
    EmpDetailList = []
    
file = open("employeeinfo.txt", "r")
data = file.readlines()

condition = True

if fromdate.upper() == 'ALL':
    condition = False
    for employee in dat:
        employee = [xstrip() for x in employee.strip().split("|")]
        
if not condition:
    EmpDetailList.append([employee[0], employee[1], employee[2],float(employee[3]), float(employee[4]), float(employee[5])])
    else:
if fromdate == employee[0]:
    EmpDetailList.append([employee[0], employee[1], employee[2],float(employee[3]), float(employee[4]), float(employee[5])])
    return EmpDetailList
if __name__ == "__main__":
    EmpDetailList = []
EmpTotals = {}
while True:
    empname= GetEmpName()
    if (emp.upper() == "END"):
        break
    fromdate, todate = GetDatesWorked()
    hours = GetHoursWorked()
    hourlyrate = GetHOurslyRate()
    taxrate = GetTaxRate()
    
    print()
    print()
    fromdate = GetFromDate()
    
EmpDetailList = ReadEmployeeInformation(fromdate)

print()
printinfo(EmpDetailList)
print()
PrintTotals(EmpTotals)
    

        