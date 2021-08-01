import cloudconvert
api="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiYTRiNWI5OWQ3MGZmZTdjNmZjMjY2YTI1MjkwZjRkOWZmMGZiZGRmZTIxNTUyMDY4YWMwZGNjOThhN2JlNzRkNjlhZjhiNDhmMzNmMjZhMTEiLCJpYXQiOjE2MjcxODA1NTguNzcyMjQzLCJuYmYiOjE2MjcxODA1NTguNzcyMjQ1LCJleHAiOjQ3ODI4NTQxNTguNzMzODU2LCJzdWIiOiI1MjQ3OTEyNCIsInNjb3BlcyI6WyJ1c2VyLnJlYWQiLCJwcmVzZXQud3JpdGUiLCJwcmVzZXQucmVhZCIsIndlYmhvb2sud3JpdGUiLCJ3ZWJob29rLnJlYWQiLCJ0YXNrLndyaXRlIiwidGFzay5yZWFkIiwidXNlci53cml0ZSJdfQ.rsDNdxadbLlywKEU6jAWikJzcs4AVEqGCio7HiVcaS5jMGPv--ZK8RuytH3IVE4ZJihc06GvKHXq1A89DWUups36CwU_CSxnPUMVtLNfBz-hGGikvhvwtGBeUnVhShiUYHM9Cn8Tt3J1DaIYR4-yFBsjXU_01ZO1jW7zcp9IYKQ9PlWUdqDjlEdIiFX2sGuy8ZBBYFcBGcFWhEBfFAE20nwtugjiv7YMR5WJklPk211OSXIpQdCIn6Zm7Vk5InEwnOqMdGwyYb1WES8ncfRM4AvMuMlH59OrORdDESPYx_dw9nG9nTMBa0cI8EAi3Uj79s_NoiJSSCn7qO1_yZeoaF3EgdRHvKEFCIGO6tYmiG_P0sv_NdR4cle7AOq8m6Mg3VIO9cIxB50P9N9vm2r7Wn7ylqeD7KMYkiajYiAfj6rml7X83ce9Wq1a234R3G7D10TV2z0G-j3INTJ1bIfLuCaQJPOOJ51MgYIEc_eh1Soo5crSClu-1hVMbiFLWJ_XuThDGWCCEqNoAj8JIhGs-YkXp9IzVhCpV7LGQqdC005mUgtitbjpsfsnRB7G1k-6C9cBwlED2HKwp8MfqQAJ2OCthy9woNpV867R2-wpKyDa9JqtwEgmoXDwbHPVlnew0CcNYZOUGxX5be1fRnoru-"
cloudconvert.configure(api_key=api, sandbox=False)



job = cloudconvert.Job.create(payload={
     "tasks": {
         'import-my-file': {
              'operation': 'import/url',
              'url': 'https://my-url'
         },
         'convert-my-file': {
             'operation': 'convert',
             'input': 'import-my-file',
             'output_format': 'pdf',
             'some_other_option': 'value'
         },
         'export-my-file': {
             'operation': 'export/url',
             'input': 'convert-my-file'
         }
     }
 })




for task in job["tasks"]:
    if task.get("name") == "export-it" and task.get("status") == "finished":
        export_task = task

file = export_task.get("result").get("files")[0]
cloudconvert.download(filename=file['filename'], url=file['url'])