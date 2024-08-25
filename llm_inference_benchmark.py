import time
import concurrent.futures
import requests
import json
import threading

KEY = "APIKEY"

# Define your API endpoints and associated models
API_MODELS = {
    "https://api.arliai.com/v1/chat/completions": ["Meta-Llama-3.1-70B-Instruct"]
}

SESSION = 1

# Define your prompts to test with
SHORT_PROMPTS = [
    "What is the meaning of life? Please create a very long response to try and explore this question in great detail."
]

# 4030 tokens using llama tokenizer
LONG_PROMPTS = [
    "I will give you a story that is repeated, at the end you will repeat the same story back to me only once. Story:\n\nIn the quiet town of Serenity, nestled between the towering mountains and the vast sea, lived a young boy named Eli. Eli was not your ordinary boy. He had a peculiar fascination with time and often spent hours gazing at the antique grandfather clock in his living room, its rhythmic ticking echoing through the silence of the house. His curiosity was insatiable, and he would often lose himself in the intricate mechanics of the clock, trying to decipher the secrets it held. He wondered about the passage of time, the ticking seconds that turned into minutes, the minutes that formed hours, and the hours that marked the days. He was fascinated by the concept of time, a force so powerful yet so intangible. His best friend, a clever and adventurous girl named Lily, shared his fascination with time and often joined him in his explorations.\\n\\nOne day, while Eli and Lily were examining the clock, they noticed a hidden compartment. Inside it, they found an old, dusty book titled \\\"The Secrets of Time\\\". The book was bound in leather and had pages yellowed with age. It was filled with cryptic symbols and ancient scripts, a testament to the knowledge of a bygone era. As they opened the book, a whirlwind of light enveloped them, and before they knew it, they were standing in a different era. They felt a rush of adrenaline as they realized that they had traveled back in time, a concept they had only read about in science fiction novels.\\n\\nEli and Lily found themselves in the middle of a bustling medieval market. The air was filled with the aroma of freshly baked bread and the clamor of merchants advertising their wares. They saw knights in shining armor, heard minstrels playing lutes, and watched as jesters entertained the crowd with their antics. The medieval era was a time of chivalry and honor, and Eli and Lily were fascinated by the customs and traditions of the time. They learned about the code of chivalry, the importance of honor, and the role of knights in society. They marveled at the grandeur of the castles, the intricacy of the tapestries, and the beauty of the stained glass windows. They witnessed the power of the king, the wisdom of the queen, and the bravery of the knights. They saw the hardships of the peasants, the struggles of the serfs, and the determination of the craftsmen. They even befriended a kind-hearted knight named Sir Geoffrey, who taught them the ways of the knight and shared tales of his adventures.\\n\\nDuring their time in the medieval era, Eli and Lily learned about chivalry, experienced a grand feast in a castle, and even participated in a jousting tournament. They felt the thrill of the tournament, the tension in the air, the cheers of the crowd, and the exhilaration of victory. Despite the excitement, they longed for home. They missed the peacefulness of Serenity, the comfort of their home, and the familiarity of their surroundings. Remembering the book, they opened it once again and were whisked away to another time.\\n\\nEli and Lily landed on the deck of a massive ship sailing across the vast ocean. They had arrived in the Age of Exploration. They met explorers, learned to navigate using the stars, and experienced the thrill of discovering new lands. They encountered exotic animals, tasted new foods, and learned about different cultures. The Age of Exploration was a time of discovery and adventure, and Eli and Lily were thrilled to be a part of it. They felt the excitement of the explorers as they set sail for unknown lands, the fear and anticipation as they braved the treacherous seas, and the joy and relief as they discovered new lands. They saw the diversity of the world, the richness of different cultures, and the beauty of nature in its purest form. They befriended a wise and seasoned explorer named Captain Hawkins, who shared tales of his voyages and taught them the art of navigation.\\n\\nHowever, the harsh life at sea made Eli and Lily yearn for the comforts of their home. They missed the familiar sights and sounds of Serenity, and the endless expanse of the sea made them feel small and insignificant. They longed for the comfort of their bed, the warmth of their home, and the love of their family. They opened the book once again, ready for their next adventure.\\n\\nThis time, Eli and Lily found themselves in a bustling city during the Industrial Revolution. They saw factories spewing smoke, heard the clanging of hammers on metal, and felt the rumble of machinery under their feet. They learned about the transformative power of technology and the harsh realities of labor during this era. The Industrial Revolution was a time of great change and progress, but it also brought about social and economic inequality. Eli and Lily saw the stark contrast between the wealthy factory owners and the poor factory workers, the disparity between the rich and the poor, and the struggle for rights and equality. They befriended a kind and hardworking factory worker named Molly, who shared her experiences and taught them about the realities of factory life.\\n\\nDespite the marvels of this era, Eli and Lily missed the tranquility of Serenity. They missed the quiet of their home, the gentle ticking of the grandfather clock, and the comfort of familiarity. They longed for the simplicity of their life, the innocence of their childhood, and the freedom of their youth. They opened the book one last time, hoping it would take them home.\\n\\nEli and Lily woke up to the familiar ticking of the grandfather clock. They were back in their living room in Serenity. Their journey through time had come to an end. They had seen different eras, met various people, and experienced life in different times. But in the end, they realized that there truly was no place like home. Eli and Lily looked at the book one last time before placing it back in the hidden compartment. They knew that they could always rely on it if they ever wanted to embark on another journey through time. But for now, they were content with being home, cherishing the present while knowing the past. And so, Eli and Lily's extraordinary journey through time came to an end. But the memories of their adventures would stay with them forever, reminding them of the vast tapestry of human history and their small but significant place within it. The end. (REPEAT STORY)\n\nIn the quiet town of Serenity, nestled between the towering mountains and the vast sea, lived a young boy named Eli. Eli was not your ordinary boy. He had a peculiar fascination with time and often spent hours gazing at the antique grandfather clock in his living room, its rhythmic ticking echoing through the silence of the house. His curiosity was insatiable, and he would often lose himself in the intricate mechanics of the clock, trying to decipher the secrets it held. He wondered about the passage of time, the ticking seconds that turned into minutes, the minutes that formed hours, and the hours that marked the days. He was fascinated by the concept of time, a force so powerful yet so intangible. His best friend, a clever and adventurous girl named Lily, shared his fascination with time and often joined him in his explorations.\\n\\nOne day, while Eli and Lily were examining the clock, they noticed a hidden compartment. Inside it, they found an old, dusty book titled \\\"The Secrets of Time\\\". The book was bound in leather and had pages yellowed with age. It was filled with cryptic symbols and ancient scripts, a testament to the knowledge of a bygone era. As they opened the book, a whirlwind of light enveloped them, and before they knew it, they were standing in a different era. They felt a rush of adrenaline as they realized that they had traveled back in time, a concept they had only read about in science fiction novels.\\n\\nEli and Lily found themselves in the middle of a bustling medieval market. The air was filled with the aroma of freshly baked bread and the clamor of merchants advertising their wares. They saw knights in shining armor, heard minstrels playing lutes, and watched as jesters entertained the crowd with their antics. The medieval era was a time of chivalry and honor, and Eli and Lily were fascinated by the customs and traditions of the time. They learned about the code of chivalry, the importance of honor, and the role of knights in society. They marveled at the grandeur of the castles, the intricacy of the tapestries, and the beauty of the stained glass windows. They witnessed the power of the king, the wisdom of the queen, and the bravery of the knights. They saw the hardships of the peasants, the struggles of the serfs, and the determination of the craftsmen. They even befriended a kind-hearted knight named Sir Geoffrey, who taught them the ways of the knight and shared tales of his adventures.\\n\\nDuring their time in the medieval era, Eli and Lily learned about chivalry, experienced a grand feast in a castle, and even participated in a jousting tournament. They felt the thrill of the tournament, the tension in the air, the cheers of the crowd, and the exhilaration of victory. Despite the excitement, they longed for home. They missed the peacefulness of Serenity, the comfort of their home, and the familiarity of their surroundings. Remembering the book, they opened it once again and were whisked away to another time.\\n\\nEli and Lily landed on the deck of a massive ship sailing across the vast ocean. They had arrived in the Age of Exploration. They met explorers, learned to navigate using the stars, and experienced the thrill of discovering new lands. They encountered exotic animals, tasted new foods, and learned about different cultures. The Age of Exploration was a time of discovery and adventure, and Eli and Lily were thrilled to be a part of it. They felt the excitement of the explorers as they set sail for unknown lands, the fear and anticipation as they braved the treacherous seas, and the joy and relief as they discovered new lands. They saw the diversity of the world, the richness of different cultures, and the beauty of nature in its purest form. They befriended a wise and seasoned explorer named Captain Hawkins, who shared tales of his voyages and taught them the art of navigation.\\n\\nHowever, the harsh life at sea made Eli and Lily yearn for the comforts of their home. They missed the familiar sights and sounds of Serenity, and the endless expanse of the sea made them feel small and insignificant. They longed for the comfort of their bed, the warmth of their home, and the love of their family. They opened the book once again, ready for their next adventure.\\n\\nThis time, Eli and Lily found themselves in a bustling city during the Industrial Revolution. They saw factories spewing smoke, heard the clanging of hammers on metal, and felt the rumble of machinery under their feet. They learned about the transformative power of technology and the harsh realities of labor during this era. The Industrial Revolution was a time of great change and progress, but it also brought about social and economic inequality. Eli and Lily saw the stark contrast between the wealthy factory owners and the poor factory workers, the disparity between the rich and the poor, and the struggle for rights and equality. They befriended a kind and hardworking factory worker named Molly, who shared her experiences and taught them about the realities of factory life.\\n\\nDespite the marvels of this era, Eli and Lily missed the tranquility of Serenity. They missed the quiet of their home, the gentle ticking of the grandfather clock, and the comfort of familiarity. They longed for the simplicity of their life, the innocence of their childhood, and the freedom of their youth. They opened the book one last time, hoping it would take them home.\\n\\nEli and Lily woke up to the familiar ticking of the grandfather clock. They were back in their living room in Serenity. Their journey through time had come to an end. They had seen different eras, met various people, and experienced life in different times. But in the end, they realized that there truly was no place like home. Eli and Lily looked at the book one last time before placing it back in the hidden compartment. They knew that they could always rely on it if they ever wanted to embark on another journey through time. But for now, they were content with being home, cherishing the present while knowing the past. And so, Eli and Lily's extraordinary journey through time came to an end. But the memories of their adventures would stay with them forever, reminding them of the vast tapestry of human history and their small but significant place within it. The end. (REPEAT STORY)\n\nIn the quiet town of Serenity, nestled between the towering mountains and the vast sea, lived a young boy named Eli. Eli was not your ordinary boy. He had a peculiar fascination with time and often spent hours gazing at the antique grandfather clock in his living room, its rhythmic ticking echoing through the silence of the house. His curiosity was insatiable, and he would often lose himself in the intricate mechanics of the clock, trying to decipher the secrets it held. He wondered about the passage of time, the ticking seconds that turned into minutes, the minutes that formed hours, and the hours that marked the days. He was fascinated by the concept of time, a force so powerful yet so intangible. His best friend, a clever and adventurous girl named Lily, shared his fascination with time and often joined him in his explorations.\\n\\nOne day, while Eli and Lily were examining the clock, they noticed a hidden compartment. Inside it, they found an old, dusty book titled \\\"The Secrets of Time\\\". The book was bound in leather and had pages yellowed with age. It was filled with cryptic symbols and ancient scripts, a testament to the knowledge of a bygone era. As they opened the book, a whirlwind of light enveloped them, and before they knew it, they were standing in a different era. They felt a rush of adrenaline as they realized that they had traveled back in time, a concept they had only read about in science fiction novels.\\n\\nEli and Lily found themselves in the middle of a bustling medieval market. The air was filled with the aroma of freshly baked bread and the clamor of merchants advertising their wares. They saw knights in shining armor, heard minstrels playing lutes, and watched as jesters entertained the crowd with their antics. The medieval era was a time of chivalry and honor, and Eli and Lily were fascinated by the customs and traditions of the time. They learned about the code of chivalry, the importance of honor, and the role of knights in society. They marveled at the grandeur of the castles, the intricacy of the tapestries, and the beauty of the stained glass windows. They witnessed the power of the king, the wisdom of the queen, and the bravery of the knights. They saw the hardships of the peasants, the struggles of the serfs, and the determination of the craftsmen. They even befriended a kind-hearted knight named Sir Geoffrey, who taught them the ways of the knight and shared tales of his adventures.\\n\\nDuring their time in the medieval era, Eli and Lily learned about chivalry, experienced a grand feast in a castle, and even participated in a jousting tournament. They felt the thrill of the tournament, the tension in the air, the cheers of the crowd, and the exhilaration of victory. Despite the excitement, they longed for home. They missed the peacefulness of Serenity, the comfort of their home, and the familiarity of their surroundings. Remembering the book, they opened it once again and were whisked away to another time.\\n\\nEli and Lily landed on the deck of a massive ship sailing across the vast ocean. They had arrived in the Age of Exploration. They met explorers, learned to navigate using the stars, and experienced the thrill of discovering new lands. They encountered exotic animals, tasted new foods, and learned about different cultures. The Age of Exploration was a time of discovery and adventure, and Eli and Lily were thrilled to be a part of it. They felt the excitement of the explorers as they set sail for unknown lands, the fear and anticipation as they braved the treacherous seas, and the joy and relief as they discovered new lands. They saw the diversity of the world, the richness of different cultures, and the beauty of nature in its purest form. They befriended a wise and seasoned explorer named Captain Hawkins, who shared tales of his voyages and taught them the art of navigation.\\n\\nHowever, the harsh life at sea made Eli and Lily yearn for the comforts of their home. They missed the familiar sights and sounds of Serenity, and the endless expanse of the sea made them feel small and insignificant. They longed for the comfort of their bed, the warmth of their home, and the love of their family. They opened the book once again, ready for their next adventure.\\n\\nThis time, Eli and Lily found themselves in a bustling city during the Industrial Revolution. They saw factories spewing smoke, heard the clanging of hammers on metal, and felt the rumble of machinery under their feet. They learned about the transformative power of technology and the harsh realities of labor during this era. The Industrial Revolution was a time of great change and progress, but it also brought about social and economic inequality. Eli and Lily saw the stark contrast between the wealthy factory owners and the poor factory workers, the disparity between the rich and the poor, and the struggle for rights and equality. They befriended a kind and hardworking factory worker named Molly, who shared her experiences and taught them about the realities of factory life.\\n\\nDespite the marvels of this era, Eli and Lily missed the tranquility of Serenity. They missed the quiet of their home, the gentle ticking of the grandfather clock, and the comfort of familiarity. They longed for the simplicity of their life, the innocence of their childhood, and the freedom of their youth. They opened the book one last time, hoping it would take them home.\\n\\nEli and Lily woke up to the familiar ticking of the grandfather clock. They were back in their living room in Serenity. Their journey through time had come to an end. They had seen different eras, met various people, and experienced life in different times. But in the end, they realized that there truly was no place like home. Eli and Lily looked at the book one last time before placing it back in the hidden compartment. They knew that they could always rely on it if they ever wanted to embark on another journey through time. But for now, they were content with being home, cherishing the present while knowing the past. And so, Eli and Lily's extraordinary journey through time came to an end. But the memories of their adventures would stay with them forever, reminding them of the vast tapestry of human history and their small but significant place within it. The end. (REPEAT STORY)\n\nNow repeat the story exactly as it was written again."
]

system = """
You are an intelligent assistant AI. Answer thoroughly.
""".strip()

def generation_test(i, api, model):
    total_tokens = 0
    total_time = 0
    prompt_no = 1
    for user in SHORT_PROMPTS:
        stime = time.time()
        payload = json.dumps({
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": system
                },
                {
                    "role": "user",
                    "content": user
                }
            ],
            "max_tokens": 1024,
            "temperature": 0.0
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': KEY
        }
        response = requests.request("POST", api, headers=headers, data=payload)
        api_out = response.json()
        ctime = round(time.time() - stime, ndigits=3)
        total_time += ctime
        ctokens = api_out['usage']['completion_tokens']
        itokens = api_out['usage']['prompt_tokens']
        tps = round(ctokens / ctime, ndigits=1)
        print(f"---[Thread {i}, Model: {model}, Prompt {prompt_no}, {itokens} tokens long] Generation stats: time {ctime}s, {ctokens} tokens, {tps} tokens/s---")
        total_tokens += ctokens
        prompt_no += 1
    avg_time = round(total_time / len(SHORT_PROMPTS), ndigits=3)
    return total_tokens, avg_time, tps

def ingestion_test(i, api, model):
    total_tokens = 0
    total_time = 0
    prompt_no = 1
    for user in LONG_PROMPTS:
        stime = time.time()
        payload = json.dumps({
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": system
                },
                {
                    "role": "user",
                    "content": user
                }
            ],
            "max_tokens": 1,
            "temperature": 0.0
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': KEY
        }
        response = requests.request("POST", api, headers=headers, data=payload)
        api_out = response.json()
        ctime = round(time.time() - stime, ndigits=3)
        total_time += ctime
        itokens = api_out['usage']['prompt_tokens']
        tps = round(itokens / ctime, ndigits=1)
        print(f"---[Thread {i}, Model: {model}, Prompt {prompt_no}] Ingestion stats: time {ctime}s, {itokens} tokens, {tps} tokens/s---")
        total_tokens += itokens
        prompt_no += 1
    avg_time = round(total_time / len(LONG_PROMPTS), ndigits=3)
    return total_tokens, avg_time, tps

def long_context_generation_test(i, api, model, avg_time):
    total_tokens = 0
    total_time = 0
    prompt_no = 1
    for user in LONG_PROMPTS:
        stime = time.time()
        payload = json.dumps({
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": system
                },
                {
                    "role": "user",
                    "content": user
                }
            ],
            "max_tokens": 1024,
            "temperature": 0.0
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': KEY
        }
        response = requests.request("POST", api, headers=headers, data=payload)
        api_out = response.json()
        ctime = round(time.time() - stime, ndigits=3)
        ctime = ctime - avg_time
        total_time += ctime
        ctokens = api_out['usage']['completion_tokens']
        itokens = api_out['usage']['prompt_tokens']
        tps = round(ctokens / ctime, ndigits=1)
        print(f"---[Thread {i}, Model: {model}, Prompt {prompt_no}, {itokens} tokens long] Generation stats: time {ctime}s, {ctokens} tokens, {tps} tokens/s---")
        total_tokens += ctokens
        prompt_no += 1
    avg_time = round(total_time / len(LONG_PROMPTS), ndigits=3)
    return total_tokens, avg_time, tps

#Test prompt generation
print(f"===Testing prompt generation using {SESSION} sessions and testing {len(SHORT_PROMPTS)} prompts with {len(API_MODELS)} models.===")
print()

executor = concurrent.futures.ThreadPoolExecutor(max_workers=SESSION * len(API_MODELS))
stime = time.time()

futures = [executor.submit(generation_test, i, api, model) for i in range(SESSION) for api, models in API_MODELS.items() for model in models]

concurrent.futures.wait(futures)

ctime = round(time.time() - stime, ndigits=3)
results = [future.result() for future in futures]
total_tps = round(sum(result[2] for result in results), ndigits=1)
min_tps = round(min(result[2] for result in results), ndigits=1)
max_tps = round(max(result[2] for result in results), ndigits=1)    
avg_time = round(sum(result[1] for result in results) / (SESSION * len(API_MODELS)), ndigits=3)
print()
print(f"Generated {sum(result[0] for result in results)} tokens in {ctime} seconds.")
print(f"Aggregate across all {SESSION * len(API_MODELS)} sessions: {total_tps} tokens/s")
print(f"Individual sessions: Min: {min_tps} tokens/s, Max: {max_tps} tokens/s")
print(f"Average completion time per thread: {avg_time} seconds")
print()
print()

# Test prompt ingestion
print(f"===Testing prompt ingestion using {SESSION} sessions and testing {len(LONG_PROMPTS)} prompts with {len(API_MODELS)} models.===")
print()

executor = concurrent.futures.ThreadPoolExecutor(max_workers=SESSION * len(API_MODELS))
stime = time.time()

futures = [executor.submit(ingestion_test, i, api, model) for i in range(SESSION) for api, models in API_MODELS.items() for model in models]

concurrent.futures.wait(futures)

ctime = round(time.time() - stime, ndigits=3)
results = [future.result() for future in futures]
total_tps = round(sum(result[2] for result in results), ndigits=1)
min_tps = round(min(result[2] for result in results), ndigits=1)
max_tps = round(max(result[2] for result in results), ndigits=1)     
avg_time = round(sum(result[1] for result in results) / (SESSION * len(API_MODELS)), ndigits=3)
print()
print(f"Ingested {sum(result[0] for result in results)} tokens in {ctime} seconds.")
print(f"Aggregate across all {SESSION * len(API_MODELS)} sessions: {total_tps} tokens/s")
print(f"Individual sessions: Min: {min_tps} tokens/s, Max: {max_tps} tokens/s")
print(f"Average ingestion time per session: {avg_time} seconds")
print()
print()

# Test long context generation
print(f"===Testing long context generation using {SESSION} sessions and testing {len(LONG_PROMPTS)} prompts with {len(API_MODELS)} models.===")
print()

executor = concurrent.futures.ThreadPoolExecutor(max_workers=SESSION * len(API_MODELS))
stime = time.time()

futures = [executor.submit(long_context_generation_test, i, api, model, avg_time) for i in range(SESSION) for api, models in API_MODELS.items() for model in models]

concurrent.futures.wait(futures)

ctime = round(time.time() - stime, ndigits=3)
results = [future.result() for future in futures]
total_tps = round(sum(result[2] for result in results), ndigits=1)
min_tps = round(min(result[2] for result in results), ndigits=1)
max_tps = round(max(result[2] for result in results), ndigits=1)    
avg_time = round(sum(result[1] for result in results) / (SESSION * len(API_MODELS)), ndigits=3)
print()
print(f"Generated {sum(result[0] for result in results)} tokens in {ctime} seconds.")
print(f"Aggregate across all {SESSION * len(API_MODELS)} sessions: {total_tps} tokens/s")
print(f"Individual sessions: Min: {min_tps} tokens/s, Max: {max_tps} tokens/s")
print(f"Average generation time per session: {avg_time} seconds")