import requests

def chatbot_query(user_input):
    """
    구글 Gemini API를 사용하여 사용자의 입력에 응답 생성.
    """
    # 이전에 제공한 API 키 사용
    api_key = "AIzaSyDaU67xjmxRCO-kc8niC3Reb5OprzOlUJk"  # 실제 키 사용
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [{"parts": [{"text": user_input}]}]
    }

    try:
        response = requests.post(url, headers=headers, json=data)

        response.raise_for_status()  # HTTP 에러 발생 시 예외 발생
        content = response.json()
        explanation = content['candidates'][0]['content']['parts'][0]['text']
        return explanation
    except requests.exceptions.RequestException as e:
        return f"API 요청 중 오류 발생: {e}"
    except KeyError:
        return "API 응답을 처리하는 중 오류가 발생했습니다."

def main():
    print("Google Gemini API 기반 챗봇입니다.")
    while True:
        # 사용자 입력 받기
        user_input = input("입력해주세요 (종료하려면 'q'): ").strip()
        if user_input.lower() == 'q':
            print("프로그램을 종료합니다.")
            break

        # Gemini API에 요청 보내기
        print("답변을 생성 중입니다...")
        response = chatbot_query(user_input)

        # 결과 출력
        print(f"챗봇 응답:\n{response}\n")

if __name__ == "__main__":
    main()
