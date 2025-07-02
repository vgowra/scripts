SELECT distinct FQDN AS FQDN, CONCAT(IntType, IntID) AS Interface, IF(Is_IPV6(INET6_NTOA(Address)) = 1, INET6_NTOA(Address), INET_NTOA(Address)) AS IP, Mask FROM IpAddresses
WHERE ScanId = (SELECT Scan.ScanId FROM Scan WHERE Scan.`Status` = 1 order by Scan.ScanId DESC limit 1)
#AND FQDN LIKE "%%.city.%"
AND (INET_NTOA(Address)) like "192.168.%"
#AND FQDN LIKE "%rtr01%.city%"
#AND Descr LIKE "%aabbcc%"
;
