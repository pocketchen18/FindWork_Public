from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import time
import random
def yjs_run_automation():

    input("1....按enter继续")
    # 启动 playwright driver 进程
    p = sync_playwright().start()

    input('2....按enter继续')
    # 启动浏览器，返回 Browser 类型对象

    browser = p.firefox.launch(headless=False)

    # 创建带cookies的上下文
    context = browser.new_context()

    # 添加已获取的cookies
    context.add_cookies([])

    # 创建新页面，返回 Page 类型对象
    page = context.new_page()
    # page.set_viewport_size({"width": 1000, "height": 400})
    page.goto("https://q.yingjiesheng.com/pc/searchintern")
    print(f"请稍等")
    page.wait_for_timeout(1000)
    print(page.title())  # 打印网页标题栏

    page.locator("xpath=/html/body/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div[1]/a/button/span").click()
    page.wait_for_timeout(1000)

    # 获取用户输入
    position_input = input("请输入要搜索的职位: ")

    # 在指定的输入框中填入用户输入的文字并按下回车键
    page.locator("xpath=/html/body/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/input").fill(
        position_input)
    page.locator("xpath=/html/body/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/input").press(
        "Enter")
    page.wait_for_timeout(1000)

    count_need = int(input("请输入点击立即申请的次数: "))

    # 1. 获取所有精确匹配"立即申请"的按钮（自动忽略"申请记录"等干扰项）
    apply_buttons = page.get_by_text("立即申请", exact=True).all()

    print(f"🔍 找到 {len(apply_buttons)} 个'立即申请'按钮")
    input("按enter继续")
    # 遍历并点击所有"立即申请"按钮，自动处理不同跳转类型
    for i, button in enumerate(apply_buttons):
        # 检查是否需要翻页
        if i > 0 and i % 20 == 0:
            print(f"\n🔄 准备翻页，已处理 {i} 个按钮")

            try:
                # 等待翻页按钮出现
                next_button = page.locator(
                    "#list > div.search-list > div.search-list-pagination > div > button.btn-next")
                if next_button.is_visible() and next_button.is_enabled():
                    print("✅ 翻页按钮可见，正在点击...")

                    # 点击翻页按钮
                    next_button.click(timeout=5000)
                    print("✅ 成功点击翻页按钮")

                    # 等待新页面加载完成
                    page.wait_for_load_state("networkidle", timeout=10000)
                    print("✅ 页面加载完成")

                    # 重新获取所有"立即申请"按钮
                    apply_buttons = page.get_by_text("立即申请", exact=True).all()
                    print(f"🔍 新页面找到 {len(apply_buttons)} 个'立即申请'按钮")
                else:
                    print("❌ 翻页按钮不可见或不可点击，可能已到达最后一页")

            except Exception as e:
                print(f"⚠️ 翻页失败: {str(e)}")
                # 继续处理当前页面的剩余按钮

        try:
            # 【关键1】缩短新窗口检测超时至2500ms
            with page.context.expect_page(timeout=2500) as new_page_info:
                button.click(timeout=5000)

            # 【场景1】成功捕获新窗口
            new_page = new_page_info.value
            new_page.wait_for_load_state("networkidle", timeout=8000)
            print(f"🆕 新窗口打开: {new_page.url}")
            new_page.close()
            print("✅ 新窗口已关闭")

        except PlaywrightTimeoutError:
            # 【场景2】2.5秒内无新窗口 → 处理弹窗
            print("⏳ 检测到弹窗模式，开始处理...")

            try:
                # 1. 等待弹窗出现（基础等待）
                page.wait_for_timeout(1500)  # 等待1.5秒让弹窗渲染

                # 2. 【严格按要求】使用指定XPath
                close_btn_xpath = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[3]/div[1]/div[2]/div[3]/div/div[1]/button/i"

                # 3. 等待按钮可见并点击
                page.locator(f"xpath={close_btn_xpath}").wait_for(state="visible", timeout=3000)
                print("✅ 关闭按钮已可见")

                page.locator(f"xpath={close_btn_xpath}").click(timeout=3000)
                print("✅ 成功点击关闭按钮")

                # 4. 简单验证（可选）
                page.wait_for_timeout(500)  # 等待0.5秒确认关闭

            except Exception as e:
                print(f"❌ 弹窗处理失败: {str(e)}")
                # 最简降级：尝试按ESC
                try:
                    page.keyboard.press("Escape")
                    print("✅ 通过ESC键关闭弹窗")
                except:
                    pass

    input('3....')
    # 关闭浏览器
    browser.close()
    input('4....')
    # 关闭 playwright driver 进程
    p.stop()

