import requests

headers = {'Cookie':'JSESSIONID=92A8E582489A9B2F9411B7D1EB91327A; mailstatus14012448=ok; SSO_IDT="Bearer eyJhbGciOiJBMTI4S1ciLCJjdHkiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0.WGpFdjT6fZNT9r6pelDM_-Eq0UrwrU8rsV2UY46V-5OtinLJM_ZmnA.UIIMGow_CvVX-Zi_9h2QBw.PuJUWsmFWOcLQYbSmIvANBM0vBnYCpQ0gbupRComWrzhwR2HG1hK9Nr-fTYIfGMBUDA1YwpaBHKWOUrqqhmx0YgfW0_YgqiT8mFl2TrRLrp8cdIDSZVDYlX11qF2IL2IkW59n0u3khZYs410AwARJXIFQn1sw9CgSBZW76ZwLY9UyfNByDqsPNqsD9NvYxJJgsRtZGMz6vHB6ACo_GMwa6mtlcEA2bZSWdMAyXGPl9O4VSR9OouGXyG7KavtoELZZQJUOr_HvLS7dRLx0hou8MI1wYOAUv82cRF1NnR2vOXOFRglB-tbs1rxG7G9vSwqTxDO669kWPKNA6wPa0C1XXcJLo9UcupM3e3c2TwvRus.elzM4cfhFcD8ddyB0K1Z_g"; _pk_id.2804852a3abc.ac81=4a4f757c-70f8-4454-8db1-d944a13fa736.1476772697.1.1476772719.1476772697.; _pk_ses.2804852a3abc.ac81=*'}
r = requests.get('https://ad-test1.sm.cn/uc/userDetail?uid=1061', headers=headers)

print r.text
