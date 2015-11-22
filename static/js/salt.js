/**
 * Created by Administrator on 2015/11/9.
 */

$(document).ready(function() {
    $('.zhixing').click(function() {
        var expr_form = $('.expr_form').val();
        var tgt = $('.tgt').val();
        var fun = $('.fun').val();
        var arg = $('.arg').val();
        var timenout = $('.timeout').val();
        var gzip = $('.gzip').val();
        if (tgt == ""){var tgt = $('.tgttxt').val();}
        if( ( $('select').hasClass('gzip')) !='true'){ var gzip= ''}
        if (tgt == ""){
            alert("请检查，用户id或组没有填写")
        }else{
             $(".ret").empty();
             $("#wait").css("display","block");
             $.get('/cmd', {"expr_form": expr_form,"tgt":tgt,"fun":fun,"arg":arg,"timenout":timenout,'gzip':gzip}, function(data) {
                for (var id in data) {
                    idval = data[id];
                    idval = "<p>" + idval + "</p>"
                    id = "<p>" + id + ":</p>"
                    $('.ret').append(id,idval)
                    }
                    $(".ret p").css({"padding":")","margin":"0"})
                    $(".ret p:even").css("color","blue")
                    $(".ret p:odd").css({"color":"green","margin-left":"40px"})
                    $("#wait").css("display","none");
        });
        }
    });

    $('.status').click(function(){
        var saltrun = $(this).html()
        $(".ret").empty();
        $("#wait").css("display","block");
        $.get('/status',{"saltrun":saltrun},function(data){
            for (var status in data) {
                id = data[status]
                status = "<p>" + status + ":</p>"
                id = "<p>" + id + "</p>"
                $('.ret').append(status,id)
            }
            $(".ret p").css({"padding":")","margin":"0"})
            $(".ret p:even").css("color","blue")
            $(".ret p:odd").css({"color":"green","margin-left":"40px"})
            $("#wait").css("display","none");

        })
    })
});