function bindEmailCaptchaClick(){
    $("#captcha-btn").click(function (event){
        // $this: 代表的是当前按钮的jquery对象
        var $this = $(this);
        // 阻止默认的事件
        event.preventDefault();

        var email = $("input[name='email']").val();
        $.ajax({
            // http://127.0.0.1:500 可以省略
            //"uth/captcha/email?email=xx@qq.com
            url: "/auth/captcha/email?email="+email,
            method: "GET",
            success: function (result){
                var code = result['code'];
                if(code == 200){
                    var countdown = 5; //倒计时
                    // 开始倒计时之前，就取消掉点击事件
                    $this.off("click");
                    var timer = setInterval(function (){
                        $this.text(countdown);
                        countdown -= 1;
                        // 倒计时结束的时候执行
                        if(countdown <= 0){
                            //清掉定时器
                            clearInterval(timer);
                            // 将按钮的文字更改回来
                            $this.text("获取验证码");
                            // 倒计时结束后重新绑定点击事件
                            bindEmailCaptchaClick();
                        }
                    }, 1000);
                    // alert("邮箱验证码发送成功！");
                }else{
                    alert(result['message']);
                }
            },
            fail: function (error){
                console.log(error);
            }
        })
    });
}


// 整个网页都加载完毕后在执行
$(function (){
    bindEmailCaptchaClick();
});


// 注册表单提交事件
$('#register-form').submit(function(e) {
    e.preventDefault(); // 阻止默认表单提交行为
    
    // 发送异步请求
    $.ajax({
      url: $(this).attr('action'),
      method: 'POST',
      data: $(this).serialize(),
      success: function(response) {
        // 注册成功
        if (response === 'success') {
          alert('注册成功');
        }
        // 注册失败
        else {
          var errors = response.errors;
          var errorMessages = [];
          for (var field in errors) {
            errorMessages.push(errors[field][0]);
          }
          alert(errorMessages.join('\n'));
        }
      },
      error: function() {
        alert('发生错误，请重试');
      }
    });
  });
  