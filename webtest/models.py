from django.db import models
from db.base_model import BaseModel


class WebCaseList(BaseModel):
    web_case_title = models.CharField(max_length=200)

    def __str__(self):
        return self.web_case_title


class WebCaseStep(BaseModel):
    web_case_id = models.ForeignKey(WebCaseList)  # 这种外键的后面不要加id
    test_step_name = models.CharField(max_length=200)

    locate_choices = (

        (0, ""),
        (1, "id"),
        (2, "xpath"),
        (3, "linktext"),
        (4, "css_selector"),
        (5, "class_name"),
        (6, "name"),
        (7, "tag_name"),

    )
    locate_method = models.IntegerField(verbose_name="元素定位方法", choices=locate_choices, default=0)  # 这个需要做成枚举值
    element_value = models.CharField(max_length=200, null=True, blank=True)

    operate_choices = (
        (1, "open_brower"),
        (2, "open_url"),
        (3, "send_keys"),
        (4, "click"),
        (5, "switch_window"),
        (6, "alert"),
        (7, "switch_frame"),
        (8, "switch_default_content"),
        (9, "assert_text"),
        (10, "refresh"),
        (11, "sleep"),
        (12, "setup_login"),
    )
    operate_method = models.IntegerField(verbose_name="操作方法", choices=operate_choices, default=4)  # 这个需要做成枚举值
    test_data = models.CharField(max_length=200, null=True, blank=True)
    assert_data = models.CharField(max_length=200, null=True, blank=True)
    order_num = models.IntegerField()

    def __str__(self):
        return self.test_step_name


class WebPageElements(BaseModel):
    page_name = models.CharField(max_length=200,)
    element_name = models.CharField(max_length=200,)
    locate_choices = (
        (0, ""),
        (1, "id"),
        (2, "xpath"),
        (3, "linktext"),
        (4, "css_selector"),
        (5, "class_name"),
        (6, "name"),
        (7, "tag_name"),

    )
    locate_method = models.IntegerField(verbose_name="元素定位方法", choices=locate_choices, default=0)  # 这个需要做成枚举值
    element_value = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.element_name

#
# class WebPageOperation(BaseModel):
#     operation_name = models.CharField(max_length=200)
#     element_name = models.ForeignKey(WebPageElements)
#     operate_choices = (
#         (1, "open_brower"),
#         (2, "open_url"),
#         (3, "send_keys"),
#         (4, "click"),
#         (5, "switch_window"),
#         (6, "alert"),
#         (7, "switch_frame"),
#         (8, "switch_default_content"),
#         (9, "assert_text"),
#         (10, "refresh"),
#         (11, "sleep"),
#         (12, "setup_login"),
#     )
#     operate_method = models.IntegerField(verbose_name="操作方法", choices=operate_choices, default=4)  # 这个需要做成枚举值
#     test_data = models.CharField(max_length=200, null=True, blank=True)
#     assert_data = models.CharField(max_length=200, null=True, blank=True)
#     order_num = models.IntegerField()
#
#     def __str__(self):
#         return self.operation_name
#
#


class WebCaseStep2(BaseModel):
    web_case_id = models.ForeignKey(WebCaseList)  # 这种外键的后面不要加id
    test_step_name = models.CharField(max_length=200)
    element_name = models.ForeignKey(WebPageElements)
    operation_case_id = models.IntegerField()
    operate_choices = (
        (1, "open_brower"),
        (2, "open_url"),
        (3, "send_keys"),
        (4, "click"),
        (5, "switch_window"),
        (6, "alert"),
        (7, "switch_frame"),
        (8, "switch_default_content"),
        (9, "assert_text"),
        (10, "refresh"),
        (11, "sleep"),
        (12, "setup_login"),
    )
    operate_method = models.IntegerField(verbose_name="操作方法", choices=operate_choices, default=4)  # 这个需要做成枚举值
    test_data = models.CharField(max_length=200, null=True, blank=True)
    assert_data = models.CharField(max_length=200, null=True, blank=True)
    order_num = models.IntegerField()

    def __str__(self):
        return self.test_step_name


