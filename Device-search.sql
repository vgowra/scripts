SELECT distinct FQDN AS FQDN, CONCAT(IntType, IntID) AS Interface, IntStatus AS IntStatus, Descr AS Description FROM Interfaces
WHERE ScanId = (SELECT Scan.ScanId FROM Scan WHERE Scan.`Status` = 1 order by Scan.ScanId DESC limit 1)
AND FQDN LIKE "rtr01%.%.%.%"
#AND Concat(IntType, IntID) LIKE "%Ethernet1"
#AND Descr LIKE "%ar%"
;
