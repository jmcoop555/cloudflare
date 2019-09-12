# cloudflare

Using the CloudFlare API via Python, I needed to quickly export and review the active WAF rules for a top level domain.
zoneWafPackages.py provides a print out of WAF rule sets and their active mode status. 
<br><br> 
The goal is to audit several hundred websites via scripting and re-apply the minimum protective rules on any sites failing the security compliance check.  
<br><br>
Sample code dependency:  <a href="https://github.com/cloudflare/python-cloudflare">python-cloudflare</a>, a Python wrapper providing full access to the CloudFlare v4 API.
