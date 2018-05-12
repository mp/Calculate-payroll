# An business with multiple employees.
# If employee works > 40 hours a week pay x1.5 for over time.
# Get hours worked and pay rate

# GLOBAL CONSTANTS
BASE_HOURS = 40     # Base hours per week
OT_MULTIPLIER = 1.5 # Overtime muliplier

# Main function has #hours worked and hourly pay rate.

def main():
  hours_worked = float(input('Enter the number of hours worked'))
  pay_rate = float(input('Enter the pay rate'))
  
  if hours_worked > BASE_HOURS:
    calc_pay_with_OT(hours_worked, pay_rate)
  else:
    calc_pay_without_OT(hours_worked, pay_rate)
    
def calc_pay_without_OT(hours_worked, pay_rate):
  gross_pay = hours_worked * pay_rate
  print('The gross pay is £', format(gross_pay, ',.2f'), sep='')

def calc_pay_with_OT(hours_worked, pay_rate):
  extra_hours = hours_worked - BASE_HOURS
  gross_pay =  (40 * pay_rate) + (extra_hours * (pay_rate * OT_MULTIPLIER))
  
  print('The gross pay is £', format(gross_pay, ',.2f'), sep='')

main()