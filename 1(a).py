eno = eval(input('Enter employee number:'))
ename = input('Enter employee Name:')
ebasic = eval(input('Enter Basic Pay of the employee:'))
pf = ebasic * 12/100
allo = ebasic * 15/100
da = ebasic * 10/100
grosspay = ebasic+allo+da+pf
netpay = (ebasic+allo+da)
print('\n Employee payslip generation')
print('-------------------------------------------')
print('employee number:\t',eno)
print('employee name:\t',ename)
print('Basic:\t',pf)
print('Provident Fund(PF):\t',pf)
print('Dearness Allowance(DA):\t',da)
print('Other Allowances:\t',allo)
print('Net Salary:\t',grosspay)
