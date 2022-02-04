import pandas as pd

salary = [169.5, 211.1, 169.5, 157.3, 541.9]
workers = ['Иван', 'Алиса', 'Боб', 'Иван', 'Петр']
salary_s = pd.Series(salary,
                     index=workers,
                     name='salary',
                     dtype='float32') \
    .set_flags(allows_duplicate_labels=False)

print(salary_s)
# print(salary_s.iloc[0:3])
# print(salary_s.loc[0:3])
# print(salary_s.iloc['Алиса':'Петр'])
print(salary_s.loc['Иван':'Боб'])
# print(salary_s.loc['Иван':'Петр'])
# print(salary_s.loc['Алиса':'Петр'])
# print(salary_s.loc['Боб':])