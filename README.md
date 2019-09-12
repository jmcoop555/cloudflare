# cloudflare

Using the CloudFlare API via Python, I needed to quickly export and review the active WAF rules for a top level domain.
zoneWafPackages.py provides a print out of WAF rule sets and the active mode of rules.  The goal is to audit several hundred websites via scripting determine the delta from the minimum application security standard. Then re-apply the minimum protective rules on any sites failing the security compliance check.  
<br><br>
Sample code dependency:  <a href="https://github.com/cloudflare/python-cloudflare">python-cloudflare</a>, a Python wrapper providing full access to the CloudFlare v4 API.
