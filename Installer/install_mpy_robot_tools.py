import ubinascii, os, machine,uhashlib
from ubinascii import hexlify

encoded=(('pyhuskylens.mpy', ('TQUCHyCLfOwQUgAHQi4uL21weV9yb2JvdF90b29scy9weWh1c2t5bGVucy5weTkoMDkjVHRlJUWAHR8fHytmJCQkJCQkJCREJCRkIIsUixKLrgCAEBBzbGVlcF9tcxAQdGlja3NfbXMqAhsIdGltZRwFFgEcBRYBWYBRGwxzdHJ1Y3QWAYAQAEgqARsAcxwASBYASFmAEAphdGFuMhAOZGVncmVlcyoCGwhtYXRoHAUWARwFFgFZSBMAgBAIcG9ydCoBGwZodWIcAxYBWUoVAFmAEBRVQVJURGV2aWNlKgEbJHB5YnJpY2tzLmlvZGV2aWNlcxwDFgFZSgEAXTICFghieXRlIwAWDEhFQURFUiMBFgxGQUlMRUQyAxEAfKAiPjQCNAEwHhYOUkVRVUVTVBYcUkVRVUVTVF9CTE9DS1MWHFJFUVVFU1RfQVJST1dTFh5SRVFVRVNUX0xFQVJORUQWLFJFUVVFU1RfQkxPQ0tTX0xFQVJORUQWLFJFUVVFU1RfQVJST1dTX0xFQVJORUQWGlJFUVVFU1RfQllfSUQWKFJFUVVFU1RfQkxPQ0tTX0JZX0lEFihSRVFVRVNUX0FSUk9XU19CWV9JRBYWUkVUVVJOX0lORk8WGFJFVFVSTl9CTE9DSxYYUkVUVVJOX0FSUk9XFhpSRVFVRVNUX0tOT0NLFiJSRVFVRVNUX0FMR09SSVRITRYSUkVUVVJOX09LFiZSRVFVRVNUX0NVU1RPTU5BTUVTFhpSRVFVRVNUX1BIT1RPFiRSRVFVRVNUX1NFTkRfUEhPVE8WLlJFUVVFU1RfU0VORF9LTk9XTEVER0VTFjRSRVFVRVNUX1JFQ0VJVkVfS05PV0xFREdFUxYmUkVRVUVTVF9DVVNUT01fVEVYVBYkUkVRVUVTVF9DTEVBUl9URVhUFhpSRVFVRVNUX0xFQVJOFhxSRVFVRVNUX0ZPUkdFVBYuUkVRVUVTVF9TRU5EX1NDUkVFTlNIT1QWLlJFUVVFU1RfU0FWRV9TQ1JFRU5TSE9UFjxSRVFVRVNUX0xPQURfQUlfRlJBTUVfRlJPTV9VU0IWHFJFUVVFU1RfSVNfUFJPFjBSRVFVRVNUX0ZJUk1XQVJFX1ZFUlNJT04WFlJFVFVSTl9CVVNZEQUWGlJFVFVSTl9JU19QUk+AFjRBTEdPUklUSE1fRkFDRV9S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\n'), 'b7f678b76ccb89e55819dbde457a0d9c3b247bb640b2f1c80049d9e3e544e212'), ('rc.mpy', ('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\n'), '5a1d3530b6cc7b48e32a03c8657de18e6250f68db1665e568c67ba0d6529f1fe'), ('__init__.mpy', ('TQUCHyAkAAoABzwuLi9tcHlfcm9ib3RfdG9vbHMvX19pbml0X18ucHkAUWMAAA==\n',), 'bd0eb1ec00392c81347ab95950ebc33661aa1cb23009054638ed4cbea66fcc3e'), ('bt.mpy', ('TQUCHyCSBHieAgAHMC4uL21weV9yb2JvdF90b29scy9idC5weTAoMDlIICcnJycnJycnJycnJycnjAluJCQkJCQkJCQkJCRnJCQkJiYmJiYnJiaHGC0tLS0taSBpIENtQI0ghQplQIUKmy6LH44kAIAQCkltYWdlKgEbBmh1YhwDFgFZgFEbDHN0cnVjdBYBgBAQc2xlZXBfbXMqARsKdXRpbWUcAxYBWYAQAEgQEHNjaGVkdWxlKgIbAHMcAEgWAEgcARYBWYBRGxR1Ymx1ZXRvb3RoFgERCyMANAERASMBNAERASMCNAERASMDNAERASMENAERASMFNAERASMGNAERASMHNAERASMINAERASMJNAERASMKNAERASMLNAERASMMNAERASMNNAERASMONAErDxYcQ09OTkVDVF9JTUFHRVMjDxEATBEFNAHdRDOAgxYgX0lSUV9HQVRUU19XUklURYUWIF9JUlFfU0NBTl9SRVNVTFSGFhxfSVJRX1NDQU5fRE9ORYcWLl9JUlFfUEVSSVBIRVJBTF9DT05ORUNUiBY0X0lSUV9QRVJJUEhFUkFMX0RJU0NPTk5FQ1SJFjJfSVJRX0dBVFRDX1NFUlZJQ0VfUkVTVUxUixZAX0lSUV9HQVRUQ19DSEFSQUNURVJJU1RJQ19SRVNVTFSPFixfSVJRX0dBVFRDX1JFQURfUkVTVUxUkhYiX0lSUV9HQVRUQ19OT1RJRlmMFjxfSVJRX0dBVFRDX0NIQVJBQ1RFUklTVElDX0RPTkWKFi5fSVJRX0dBVFRDX1NFUlZJQ0VfRE9ORZEWKl9JUlFfR0FUVENfV1JJVEVfRE9ORUJEgIQWF5AWF6AWFyKAQBYXIoEAFhciggAWFyKEABYXIpAAFhcigMAAFhcioAAWFyKEABYXIoSAABYXERkUCFVVSUQjEDYBFhRfVUFSVF9VVUlEEQUUBSMRNgEWGl9VQVJUX1RYX1VVSUQRBRQFIxI2ARYaX1VBUlRfUlhfVVVJRBEFFAUjEzYBFiRfTEVHT19TRVJWSUNFX1VVSUQRBRQFIxQ2ARYkX0xFR09fU0VSVklDRV9DSEFSEQuQKgIWEF9VQVJUX1RYEQ2MKgIWEF9VQVJUX1JYERERBxEFKgIqAhYaX1VBUlRfU0VSVklDRVBQUVGAKgVTMxUWKF9hZHZlcnRpc2lu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EUZvdW5kIHBlcmlwaGVyYWw6cx5ObyB1YXJ0IHBlcmlwaGVyYWwgJ3t9JyBmb3VuZC5zEEZvdW5kIFNNQVJUIEh1YjpzFUxFR08gU21hcnQgaHViIGZvdW5kLnMmRmFpbGVkIHRvIGZpbmQgcmVxdWVzdGVkIGdhdHQgcw==\n', 'ZXJ2aWNlLnMOTmV3IGNvbm5lY3Rpb25zDERpc2Nvbm5lY3RlZHMdVW5oYW5kbGVkIGV2ZW50LCBubyBwcm9ibGVtOiBcKg4wZGlzY292ZXJfY2hhcmFjdGVyaXN0aWNzMC4uL21weV9yb2JvdF90b29scy9idC5weZBOALATExQ8Z2F0dGNfZGlzY292ZXJfY2hhcmFjdGVyaXN0aWNzsVM3AFlRYwAAAIkAPYEUuwEQEmFkdmVydGlzZQeQUSgAEgB7IwM0AVmwEwcUGmdhcF9hZHZlcnRpc2WyEBBhZHZfZGF0YbE2ggFZUWMBAACJDnBheWxvYWQWaW50ZXJ2YWxfdXNzFFN0YXJ0aW5nIGFkdmVydGlzaW5nSCsOEG9uX3dyaXRlDZBVALKwEx+xVlFjAAAAiRh2YWx1ZV9oYW5kbGUQY2FsbGJhY2uBcOAFFAxub3RpZnkJkFkkUCkAs0QQgLATFRQYZ2F0dHNfbm90aWZ5s7KxNgNZQhmAsBMvX0sRAMOwEwUUBbOysTYDWULsf1FjAAAAiSEUdmFsX2hhbmRsZRZjb25uX2hhbmRsZYJUORYqcmVnaXN0ZXJfdWFydF9zZXJ2aWNlD5BgVDMuLgCwEw0ULmdhdHRzX3JlZ2lzdGVyX3NlcnZpY2VzEhpfVUFSVF9TRVJWSUNFKgE2ATABMALBwrATBRQWZ2F0dHNfd3JpdGWyEgBCIoBkNAE2AlmwEwMUIGdhdHRzX3NldF9idWZmZXKyIoBkNgJZsBMDFAOxIoBkNgJZsbIqAmMAAACJgQQpDghzY2FuDZBpALATBxQQZ2FwX3NjYW4igZwgIoHqMCKB6jA2A1lRYwAAAIlYGQ4Sc3RvcF9zY2FuB5BsALATBxQHUTYBWVFjAAAAiYUUuIUBMhhjb25uZWN0X3VhcnQHkG9FJSUlJSUlJSUnJigpJywnKioAsbAYGF9zZWFyY2hfbmFtZVKwGB5jb25uZWN0aW5nX3VhcnRRsBgYX2Nvbm5faGFuZGxlUbAYGl9zdGFydF9oYW5kbGVRsBgWX2VuZF9oYW5kbGVRsBgUX3J4X2hhbmRsZVGwGBRfdHhfaGFuZGxlUbAYFF9hZGRyX3R5cGVRsBgKX2FkZHKwFB02AFmAQh+AV8QSAHsjBDQBWRIQc2xlZXBfbXMig3Q0AVmwExNDA4BCCICB5VeU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\n'), '0815136b5286fa7278b82cae9e4a939cee339c0f1484ab3ea862f78818959179'), ('light_matrix.mpy', ('TQUCHyCnXDiYBAAHRC4uL21weV9yb2JvdF90b29scy9saWdodF9tYXRyaXgucHk5KFAkJCREIiAoKCgoTCAoKCgoTCAoKCgoTCAoKCgoTCAoKCgoTCAoKCgoTCAoKCgoTCAoKCgoTCAoKCgoTCAoKCgobyAiICsrKytPICsrKytPICsrKytPICsrKytPICsrKytPICsrKytPICsrKytPICsrKytPICsrKytPICsrKytyIIUWhSkAgBAOZGlzcGxheRAKSW1hZ2UqAhsGaHViHAUWARwFFgFZgFEbCnV0aW1lFgGAEBJyYW5kcmFuZ2UqARsMcmFuZG9tHAMWAVmAFgAIiBYCT4YWAniJFgJCLAoRAAgRAAgrAhEACBEACCsCEQAIEQAIKwIRAAgRAAgrAhEACBEACCsCKwWAYhEACBEFKwIRAREBKwIRAAgRASsCEQAIEQErAhEACBEBKwIrBYFiEQERASsCEQAIEQErAhEBEQErAhEBEQAIKwIRAREBKwIrBYJiEQERASsCEQAIEQErAhEBEQErAhEACBEBKwIRAREBKwIrBYNiEQERAAgrAhEBEQAIKwIRAREBKwIRAAgRASsCEQAIEQErAisFhGIRAREBKwIRAREACCsCEQERASsCEQAIEQErAhEBEQErAisFhWIRAREACCsCEQERAAgrAhEBEQErAhEBEQErAhEBEQErAisFhmIRAREBKwIRAAgRASsCEQERAAgrAhEBEQAIKwIRAREACCsCKwWHYhEBEQErAhEBEQErAhEFEQErAhEDEQErAhEBEQErAisFiGIRAREBKwIRAREBKwIRAREBKwIRAAgRASsCEQERASsCKwWJYhYOdGVuc19weCwKEQcRAREBKwMRAREACBEBKwMRAREACBEBKwMRAREACBEBKwMRAREBEQErAysFgGIRAAgRAREACCsDEQERAREACCsDEQAIEQERAAgrAxEACBEBEQAIKwMRAREBEQErAysFgWIRAREBEQErAxEACBEACBEBKwMRAREBEQErAxEBEQAIEQAIKwMRAREBEQErAysFgmIRAREBEQErAxEACBEACBEBKwMRAREBEQErAxEACBEACBEBKwMRAREBEQErAysFg2IRAREACBEBKwMRAREACBEBKwMRAREBEQErAxEACBEACBEBKwMRAAgRAAgRASsDKwWEYhEBEQERASsDEQERAAgRAAgrAxEBEQERASsDEQAIEQAIEQErAxEBEQERASsDKwWFYhEBEQERASsDEQERAAgRAAgrAxEBEQERASsDEQERAAgRASsDEQERAREBKwMrBYZiEQERAREBKwMRAAgRAAgRASsDEQAIEQERAAgrAxEACA==\n', 'EQERAAgrAxEACBEBEQAIKwMrBYdiEQERAREBKwMRAREACBEBKwMRAREBEQErAxEBEQAIEQErAxEBEQERASsDKwWIYhEBEQERASsDEQERAAgRASsDEQERAREBKwMRAAgRAAgRASsDEQERAREBKwMrBYliFhB1bml0c19weDIAFhBpbWFnZV85OTIBFhJjb2RlbGluZXNUMgIQFkxNQW5pbWF0aW9uNAIWAVFjAAOEKF0mBR2AnCgjVGZGJyREIyZ9LgASGSMBNAHBSBkAgLBXW9pGB4AigGPaQgKAWllDAoCxY0oHAFmxY0oBAF0SAF6wNAHAsIr4wrCK9sMrAMSAQhiAV8W0Eg+zVbVVEg2yVbVV8isB5cSB5VeF10Pif1kQAjoUAGgyArQ0ATYBxhIHtjQBYwEBDG51bWJlcnMdMDAwMDA6MDkwOTA6MDA5MDA6MDkwOTA6MDAwMDCBEFEOFDxsaXN0Y29tcD4NgK4AKwCwX0sTAMEQAAEUAGgyAbE0ATYBLxRC6n9jAAEABXRBDgMDgK4AKwCwX0sMAMESAJexNAEvFELxf2MAAAAFhxDwQEQTA4CyYGAfJ0MiIEMnJyZDJm0mJiZDJkxKIiMoLCojAICAgICAKwWAgICAgCsFgICAgIArBYCAgICAKwWAgICAgCsFKwXAsGdZgMFCVYASG4Y0AcKygEIWgFfDhrCxVbNWsGdZibCxVbNWsGdZgeVYWtdD5H9ZWbKF10QhgIBCFoBXxImwsVWyVrBnWYCwsVWyVrBnWYHlV4bXQ+R/WbGB5cGxhddDpX+BxUIogLAUAHiANgFZsICAgICAKwUrAeXAsYDYRASAsYHmwbBnWRIBgjQBxbVD1H9Cbn9RYwAAgTQIFhUFjNuAFIkHABEAFxYAFhADFgAajCoBUzMAFgARUSoBUzMBFhx1cGRhdGVfZGlzcGxheVFjAAKBZKsBFgARBYDwJS4sJQCxsBgMZnJhbWVzEgBeIodosvc0AbAYEGludGVydmFsEiUUEHRpY2tzX21zNgCwGBRzdGFydF90aW1lgLAYHm5leHRfZnJhbWVfdGltZYCwGBpjdXJyZW50X2ZyYW1lUWMAAACJDQZmcHOIXNoBLhMTgPckNSkfRzAqUTAqUSw1KzFFALFDFYASERQUdGlja3NfZGlmZhIDFBM2ALATEzYCwbGwExPbRNmAgICAgIArBYCAgICAKwWAgICAgCsFgICAgIArBYCAgICAKwUrBcIQABkSAEywExE0Ad1EG4ASAHSwEwE0AcKwVxMDsBMV5VoYA0JtgBIAa7ATBYBVNAGC2EQbgLATAbATFVXCsFcTBbATB+VaGANCIYCwEwewEwdVgVXCsA==\n', 'VxMFsBMFsBMFVYBV5VoYBbBXEwOB5VoYAbATARIAa7ATBTQB20QFgICwGAMSMxQIc2hvdxIlECcUAGgyArI0ATYBNAE2AVlRYwABAIkIdGltZYEQUQ4nHZAKACsAsF9LEwDBEAABFABoMgGxNAE2AS8UQup/YwABAAV0QQ4DA5AKACsAsF9LDADBEgCXsTQBLxRC8X9jAAAABQ==\n'), '840f1af2a2068017d08d8f3315a3eab73db21021a79a571463fb49236e801974'), ('ctrl_plus.mpy', ('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\n'), '755e50bef444102272dc68fb20d8e697c139bc2275f2a5dcffd3bd4ddd93cde7'), ('helpers.mpy', ('TQUCHyCCTBAcAAc6Li4vbXB5X3JvYm90X3Rvb2xzL2hlbHBlcnMucHkgUG6LB4UMJEQAgBAIcG9ydCoBGwZodWIcAxYBWSL/HCKAZCoCUzMBFhJjbGFtcF9pbnSAIwAqAlMzAhYYdHJhY2tfdGFyZ2V0MgMWCnNjYWxlgBYOX19NU0hVQoEWFF9fUFlCUklDS1NUMgQQDlBCTW90b3I0AhYBUWMBBGYDMS41eLOAAQ4LEWAgABIGbWF4EgZtaW4SAF6wNAGyNAKxNAJjAAACbgpmbG9vcg5jZWlsaW5ngSzDgAEUFw2ABykkTgCwFABWNgCBVcOwFAZwd20SEbOx87LR9DQBNgFZs2MAAAptb3Rvcgx0YXJnZXQIZ2FpboEoMxIfDYAOgAkAEgpmbG9hdLCxgFXzNAGxgVWxgFXz97KBVbKAVfP0soBV8mMAAAZ2YWwGc3JjBmRzdIIUCCQjC4wdYGCFFGVgZWVghQ4AEQAXFgAWEAMWABoyARYAETICFgRkYzIDFhJhYnNfYW5nbGUyBBYKYW5nbGUyBRYWcmVzZXRfYW5nbGUjACoBUzMGFiFRYwEGZgMxLjWEdCoqABENgCQnJysqKCUqKCUqSCdVSAASAEyxNAHCIwKy3UQVgLETHF9tb3Rvcl93cmFwcGVyEx+wGAESMbAYAJ5CWoAQAFay3UQPgLGwGAMSA7AYAJ5CQ4AQEnJ1bl9hbmdsZbLdRA+AsbAYBRIzsBgAnkIsgBAAoLLdRByAEgewGACeEgBQEApwb3J0LrHyEAwubW90b3LyNAGwGAlCCIASAHsjAzQBWbAUEzYAWVFjAgAAiQNzDl9tb3Rvcl93cmFwcGVycxJVbmtub3duIG1vdG9yIHR5cGWCFCoUGROAOCszKwCwEwCeEg3ZRBOAsBMHFC0SLbE0ATYBWUIZgLATAJ4SE9lEDoCwEwcUDbE2AVlCAIBRYwAAAIkIZHV0eVQRDh8RgD4AsBMJFABWNgCCVWMAAACJgXQRFB8FgEErLCsAsBMAnhIT2UQMgLATBxQAVjYAgVVjsBMAnhIP2UQNgLATAxQJNgBZQgCAUWMAAACJg3ixgIBAHhULgEkrKywoJk4wKwCwEwCeEgvZREOAEgBrsTQBgNlEKICwEwkUAFY2AIJVwrIigTTYRAaAsiKCaObCsBMBFAxwcmVzZXSyNgFZQg2AsBMDFAOxgFU2AVlCGoCwEwCeEg3ZRA+AsBMFFAuxUzcAWUIAgFFjAAAAiYIMswEWIQ2AVSuPBysAsBMAnhIN2UQPgBIFsBMJsbI0A1lCGYCwEwCeEgvZRA6AsBMDFAWxNgFZQgCAUWMAAACJMTE=\n',), '484861e26a6633fad32f8658dabbfff5dd54fae05ba1ddc2af7b5ee5bbed956f'), ('motor_sync.mpy', ('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\n'), '7a0d139266d540d5865712a8668b07cf32eb81480bcb6f05522f8067127d1e38'))

def calc_hash(b):
    return hexlify(uhashlib.sha256(b).digest()).decode()

error=False
try:
    os.mkdir('/projects/mpy_robot_tools')
except:
    pass

for file, code, hash_gen in encoded:
    print("Writing file ", file)
    # hash_gen=code[1]
    target_loc = '/projects/mpy_robot_tools/'+file
    
    print('writing '+file+' to folder /projects/mpy_robot_tools')
    with open(target_loc,'wb') as f:
        for chunk in code:
            f.write(ubinascii.a2b_base64(chunk))
    del code

    try:
        print('Finished writing '+file+', Checking hash.')
        result=open(target_loc,'rb').read()
        hash_check=calc_hash(result)

        print('Hash generated: ',hash_gen)

        if hash_check != hash_gen:
            print('Failed hash of .mpy on SPIKE: '+hash_check)
            error=True
    except Exception as e:
        print(e)


if not error:
    print('Library written succesfully. Resetting....')
    machine.reset()
else:
    print('Failure in writing library!')