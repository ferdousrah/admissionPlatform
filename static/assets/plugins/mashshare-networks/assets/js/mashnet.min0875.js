jQuery(document).ready(function(a){function b(a){c(),jQuery(".mashnet_pinterest_header").fadeIn(500),jQuery(".mashnet_pinterest_inner").html(a),jQuery(".mashnet_pinterest_close").click(function(a){a.preventDefault(),jQuery(".mashnet_pinterest_header").hide()})}function c(){var a=window.innerWidth,b=350,c=310;if(330>=a)var b=310;if(a>400)var b=390;if(a>500)var b=490;var d=window.innerHeight/2-c/2,e=window.innerWidth/2-b/2,f='<div class="mashnet_pinterest_header" style="position:fixed;z-index:999999;max-width:'+b+"px; margin-left:"+e+"px;top:"+d+'px;">\n                        <div class="mashnet_pinit_wrapper" style="background-color:white;"><span class="mashnet_pin_it">Pin it! </span><span class="mashnet_pinicon"></span> \n<div class="mashnet_pinterest_close" style="float:right;"><a href="#">X</a></div></div>\n<div class="mashnet_pinterest_inner"></div>\n                </div>\n                ';jQuery("body").append(f)}function d(a){if(void 0===mashnet)return!1;var b=jQuery("img").not("[nopin='nopin']"),c=mashnet.pinterest_image,d=mashnet.pinterest_desc,e='<li><a target="_blank" id="mashnetPinterestPopup" href="https://pinterest.com/pin/create/button/?url='+encodeURIComponent(window.location.href)+"%2F&media="+c+"&description="+d+'"><img src="'+c+'"></a></li>',f=b.filter(function(){return jQuery(this).width()>70||jQuery(this).height()>70});for(i=0;i<f.length;i++)e+='<li><a target="_blank" id="mashnetPinterestPopup" href="https://pinterest.com/pin/create/button/?url='+encodeURIComponent(window.location.href)+"%2F&media="+f[i].src+"&description="+f[i].alt+'"><img src="'+f[i].src+'"></a></li>';return e}a(".mashicon-google").click(function(b){b.preventDefault(),winWidth=520,winHeight=350;var c=screen.height/2-winHeight/2,d=screen.width/2-winWidth/2,e=a(this).attr("href");window.open(e,"sharer","top="+c+",left="+d+",toolbar=0,status=0,width="+winWidth+",height="+winHeight+",resizable=yes")}),a(".mashicon-buffer").click(function(b){b.preventDefault(),console.log("buffer"),winWidth=800,winHeight=470;var c=screen.height/2-winHeight/2,d=screen.width/2-winWidth/2,e=a(this).attr("href");window.open(e,"sharer","top="+c+",left="+d+",toolbar=0,status=0,width="+winWidth+",height="+winHeight+",resizable=yes")}),a("body").off("click",".mashicon-pinterest").on("click",".mashicon-pinterest",function(c){c.preventDefault(),console.log("preventDefault:"+c),winWidth=520,winHeight=350;var e=screen.height/2-winHeight/2,f=screen.width/2-winWidth/2,g=a(this).attr("data-mashsb-url"),h=mashnet.pinterest_select;return"1"===h?(console.log("pinterest_select:"+h),void b(d(g))):(console.log("opening second sharer:"+h),void window.open(g,"sharer","top="+e+",left="+f+",toolbar=0,status=0,width="+winWidth+",height="+winHeight+",resizable=yes"))}),a(".mashicon-linkedin").click(function(b){b.preventDefault(),winWidth=520,winHeight=350;var c=screen.height/2-winHeight/2,d=screen.width/2-winWidth/2,e=a(this).attr("href");window.open(e,"sharer","top="+c+",left="+d+",toolbar=0,status=0,width="+winWidth+",height="+winHeight+",resizable=yes")}),a(".mashicon-digg").click(function(b){b.preventDefault(),winWidth=520,winHeight=350;var c=screen.height/2-winHeight/2,d=screen.width/2-winWidth/2,e=a(this).attr("href");window.open(e,"sharer","top="+c+",left="+d+",toolbar=0,status=0,width="+winWidth+",height="+winHeight+",resizable=yes")}),a(".mashicon-stumbleupon").click(function(b){b.preventDefault(),winWidth=520,winHeight=350;var c=screen.height/2-winHeight/2,d=screen.width/2-winWidth/2,e=a(this).attr("href");window.open(e,"sharer","top="+c+",left="+d+",toolbar=0,status=0,width="+winWidth+",height="+winHeight+",resizable=yes")}),a(".mashicon-vk").click(function(b){b.preventDefault(),winWidth=520,winHeight=350;var c=screen.height/2-winHeight/2,d=screen.width/2-winWidth/2,e=a(this).attr("href");window.open(e,"sharer","top="+c+",left="+d+",toolbar=0,status=0,width="+winWidth+",height="+winHeight+",resizable=yes")}),a(".mashicon-print").click(function(b){b.preventDefault(),winWidth=520,winHeight=350;var c=screen.height/2-winHeight/2,d=screen.width/2-winWidth/2,e=a(this).attr("href");window.open(e,"sharer","top="+c+",left="+d+",toolbar=0,status=0,width="+winWidth+",height="+winHeight+",resizable=yes")}),a(".mashicon-reddit").click(function(b){b.preventDefault(),winWidth=520,winHeight=820;var c=screen.height/2-winHeight/2,d=screen.width/2-winWidth/2,e=a(this).attr("href");window.open(e,"sharer","top="+c+",left="+d+",toolbar=0,status=0,width="+winWidth+",height="+winHeight+",resizable=yes")}),a(".mashicon-delicious").click(function(b){b.preventDefault(),winWidth=520,winHeight=350;var c=screen.height/2-winHeight/2,d=screen.width/2-winWidth/2,e=a(this).attr("href");window.open(e,"sharer","top="+c+",left="+d+",toolbar=0,status=0,width="+winWidth+",height="+winHeight+",resizable=yes")}),a(".mashicon-weibo").click(function(b){b.preventDefault(),winWidth=520,winHeight=350;var c=screen.height/2-winHeight/2,d=screen.width/2-winWidth/2,e=a(this).attr("href");window.open(e,"sharer","top="+c+",left="+d+",toolbar=0,status=0,width="+winWidth+",height="+winHeight+",resizable=yes")}),a(".mashicon-pocket").click(function(b){b.preventDefault(),winWidth=520,winHeight=350;var c=screen.height/2-winHeight/2,d=screen.width/2-winWidth/2,e=a(this).attr("href");window.open(e,"sharer","top="+c+",left="+d+",toolbar=0,status=0,width="+winWidth+",height="+winHeight+",resizable=yes")}),a(".mashicon-xing").click(function(b){b.preventDefault(),winWidth=520,winHeight=350;var c=screen.height/2-winHeight/2,d=screen.width/2-winWidth/2,e=a(this).attr("href");window.open(e,"sharer","top="+c+",left="+d+",toolbar=0,status=0,width="+winWidth+",height="+winHeight+",resizable=yes")}),a(".mashicon-odnoklassniki").click(function(b){b.preventDefault(),winWidth=520,winHeight=350;var c=screen.height/2-winHeight/2,d=screen.width/2-winWidth/2,e=a(this).attr("href");window.open(e,"sharer","top="+c+",left="+d+",toolbar=0,status=0,width="+winWidth+",height="+winHeight+",resizable=yes")}),a(".mashicon-managewp").click(function(b){b.preventDefault(),winWidth=520,winHeight=350;var c=screen.height/2-winHeight/2,d=screen.width/2-winWidth/2,e=a(this).attr("href");window.open(e,"sharer","top="+c+",left="+d+",toolbar=0,status=0,width="+winWidth+",height="+winHeight+",resizable=yes")}),a(".mashicon-tumblr").click(function(b){b.preventDefault(),winWidth=520,winHeight=350;var c=screen.height/2-winHeight/2,d=screen.width/2-winWidth/2,e=a(this).attr("href");window.open(e,"sharer","top="+c+",left="+d+",toolbar=0,status=0,width="+winWidth+",height="+winHeight+",resizable=yes")}),a(".mashicon-meneame").click(function(b){b.preventDefault(),winWidth=520,winHeight=350;var c=screen.height/2-winHeight/2,d=screen.width/2-winWidth/2,e=a(this).attr("href");window.open(e,"sharer","top="+c+",left="+d+",toolbar=0,status=0,width="+winWidth+",height="+winHeight+",resizable=yes")}),a(".mashicon-whatsapp").click(function(b){function c(a){return a.replace(/([.*+?^=!:${}()|\[\]\/\\])/g,"\\$1")}function d(a,b,d){return a.replace(new RegExp(c(b),"g"),d)}var e=mashsb.title,f=a(this).attr("href");"whatsapp://send?text="+d(e,"+","%20")+"%20"+mashsb.share_url;a(this).attr("href",f)}),a(".mashicon-mail").click(function(b){if("undefined"!=typeof mashnet){mashnet.subject,mashnet.body}else;var c=a(this).attr("href");a(this).attr("href",c),a(this).attr("target","_blank")}),a(".mashicon-yummly").click(function(b){b.preventDefault(),winWidth=620,winHeight=447;var c=screen.height/2-winHeight/2,d=screen.width/2-winWidth/2,e=a(this).attr("href");window.open(e,"sharer","top="+c+",left="+d+",toolbar=0,status=0,width="+winWidth+",height="+winHeight+",resizable=yes")}),a(".mashicon-frype").click(function(b){b.preventDefault(),winWidth=620,winHeight=447;var c=screen.height/2-winHeight/2,d=screen.width/2-winWidth/2,e=a(this).attr("href");window.open(e,"sharer","top="+c+",left="+d+",toolbar=0,status=0,width="+winWidth+",height="+winHeight+",resizable=yes")}),a(".mashicon-skype").click(function(b){b.preventDefault(),winWidth=620,winHeight=447;var c=screen.height/2-winHeight/2,d=screen.width/2-winWidth/2,e=a(this).attr("href");window.open(e,"sharer","top="+c+",left="+d+",toolbar=0,status=0,width="+winWidth+",height="+winHeight+",resizable=yes")}),a(".mashicon-telegram").click(function(b){b.preventDefault(),winWidth=620,winHeight=540;var c=screen.height/2-winHeight/2,d=screen.width/2-winWidth/2,e=a(this).attr("href");window.open(e,"sharer","top="+c+",left="+d+",toolbar=0,status=0,width="+winWidth+",height="+winHeight+",resizable=yes")}),a(".mashicon-flipboard").click(function(b){b.preventDefault(),winWidth=620,winHeight=540;var c=screen.height/2-winHeight/2,d=screen.width/2-winWidth/2,e=a(this).attr("href");window.open(e,"sharer","top="+c+",left="+d+",toolbar=0,status=0,width="+winWidth+",height="+winHeight+",resizable=yes")}),a(".mashicon-hackernews").click(function(b){b.preventDefault(),winWidth=620,winHeight=540;var c=screen.height/2-winHeight/2,d=screen.width/2-winWidth/2,e=a(this).attr("href");window.open(e,"sharer","top="+c+",left="+d+",toolbar=0,status=0,width="+winWidth+",height="+winHeight+",resizable=yes")})});