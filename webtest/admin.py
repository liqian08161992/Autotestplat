from django.contrib import admin
from webtest.models import WebCaseList, WebCaseStep, WebPageElements, WebCaseStep2


class WebCaseStepAdmin(admin.ModelAdmin):

    # 控制显示长度，必须在adminx的list_display变量中改为函数名
    def short_test_data(self):
        if len(str(self.test_data)) > 20:
            return '{}...'.format(str(self.test_data)[0:19])
        else:
            return str(self.test_data)

    short_test_data.allow_tags = True
    short_test_data.short_description = 'test_data'

    # 控制显示长度，必须在adminx的list_display变量中改为函数名
    def short_element_value(self):
        if len(str(self.element_value)) > 20:
            return '{}...'.format(str(self.element_value)[0:19])
        else:
            return str(self.element_value)

    short_element_value.allow_tags = True
    short_element_value.short_description = 'element_value'

    list_display = (
        "web_case_id", "test_step_name", "locate_method", short_element_value, "operate_method", short_test_data,
        "order_num"
    )
    ordering = ("-id", "-order_num")
    list_filter = ('web_case_id',)
    list_editable = ("order_num",)


admin.site.register(WebCaseList, )

admin.site.register(WebCaseStep, WebCaseStepAdmin)
admin.site.register(WebPageElements)
admin.site.register(WebCaseStep2)

