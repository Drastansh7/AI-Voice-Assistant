from openai import OpenAI
client = OpenAI(api_key='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')

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "write a resignation letter\n"
    },
    {
      "role": "assistant",
      "content": "[Your Name]\n[Your Address]\n[City, State, Zip Code]\n[Email Address]\n[Phone Number]\n[Date]\n\n[Recipient Name]\n[Company Name]\n[Company Address]\n[City, State, Zip Code]\n\nDear [Recipient Name],\n\nI am writing to inform you of my decision to resign from my position at [Company Name], effective [last working day, typically two weeks from the date of the letter]. \n\nI have greatly valued my time at [Company Name] and the opportunities for growth and development that have been provided to me during my tenure here. I have learned so much and have enjoyed working with a talented and dedicated team.\n\nHowever, after much consideration and deliberation, I have decided to pursue a new opportunity that aligns more closely with my long-term career goals. I believe this change will allow me to further develop my skills and contribute to my professional growth.\n\nI will work diligently over the next two weeks to ensure a smooth transition and complete any outstanding tasks or projects. I am committed to ensuring that all loose ends are tied up before my departure.\n\nI want to express my heartfelt gratitude for the support and guidance that I have received from my colleagues and supervisors during my time at [Company Name]. I have truly appreciated the mentorship and"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)

'''ChatCompletion(id='chatcmpl-951j7FZQwTexupXzfv7Nqbl6ykqly', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content=' camaraderie that I have experienced here.\n\nThank you once again for the opportunities that have been provided to me at [Company Name]. I will always look back on my time here with fond memories.\n\nI wish the company continued success and growth in the future.\n\nSincerely,\n\n[Your Name]', role='assistant', function_call=None, tool_calls=None))], created=1710985305, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_fa89f7a861', usage=CompletionUsage(completion_tokens=59, prompt_tokens=272, total_tokens=331))'''
