__author__ = 'David Dworin'


from refreshbooks import api

c = api.TokenClient(
    'YOUR_SITE_ADDRESS.freshbooks.com',
    'YOUR_API_TOKEN',
    user_agent='DavidsChaseExpenseFixer/1.0'
)

expenses = c.expense.list(page='100')
print "There are %s pages of expenses." % (
    expenses.expenses.attrib['pages'],
    )
for i in range(1,int(expenses.expenses.attrib['pages'])+1):
    expenses = c.expense.list(page=str(i))
    for myexpense in expenses.expenses.expense:
        print "Expense(%s) Notes: %s Vendor: %s" % (
            myexpense.expense_id,
            str(myexpense.notes).strip(),
            myexpense.vendor
            )
        if(myexpense.vendor==''):
            print "Fixing the Vendor on Expense %s" % (myexpense.expense_id)
            response = c.expense.update(
                expense=dict(
                    expense_id=myexpense.expense_id,
                    vendor=str(myexpense.notes).strip()
                )
            )

print "All Done!"