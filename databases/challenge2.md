sql_query_string = """
SELECT Teacher, COUNT(*) AS Total
FROM
(
SELECT *
FROM SCAN AS s
INNER JOIN periodAtt AS p
ON s.StudentID=p.StudentID AND substr(ScanTime, 1,inStr(ScanTime, ' ')-1)=p.Date
WHERE Attendance='A'
) AS allCuts
GROUP BY Teacher
ORDER BY Total DESC
"""
#Exectue the SQL query
result_df = sql_query_to_pd(sql_query_string, db_name='default.db')
result_df