# Databricks notebook source
import re
import json

try:
    # app service
    file_path = "./app_config/config.json"
    with open(file_path) as f:
        config_json = json.load(f)
except:
    # databricks
    file_path = "../app_config/config.json"
    with open(file_path) as f:
        config_json = json.load(f)

CONFIG_TYPE = config_json["CONFIG_TYPE"]
CONFIG_SETTING = config_json["CONFIG_SETTING"]
RUN_EXTEND_AND_VERSION = True  # get_run_extend_and_version


def filter_comment_config_json(json_path):
    with open(json_path, 'r') as f:
        data = f.read()
        data = re.sub(r'//.*?\n', '\n', data)
        data = re.sub(re.compile('/\*.*?\*/', re.DOTALL), '', data)
        parsed_data = json.loads(data)
    return parsed_data


class L3_L4_Config:
    def __init__(self):
        self.config_path = "../app_config/l3_l4_config.json"
        self.config = filter_comment_config_json(self.config_path)


class Config:
    """
    """

    def __init__(self, is_web: bool = False, web_detail_groupby: str = None):
        self.config = CONFIG_SETTING[CONFIG_TYPE]
        self.idashboard_cloud_tablename = self.config["idashboard_cloud_tablename"]
        self.idashboard_onpremise = self.config["idashboard_onpremise"]
        self.is_web = is_web
        self.web_detail_groupby = web_detail_groupby

    @property
    def IE_CONDITION_PATH(self) -> str:
        return config_json["COMMON"]["IE_CONDITION_PATH"]

    @property
    def C_RPT_COMMIT_YIELD_PATH(self) -> str:
        return config_json["COMMON"]["C_RPT_COMMIT_YIELD_PATH"]

    @property
    def N_BU_YEAR_TARGET_VIEW_PATH(self) -> str:
        return config_json["COMMON"]["N_BU_YEAR_TARGET_VIEW_PATH"]

    @property
    def l4_temp(self) -> str:
        return "l4_temp"

    @property
    def taskName(self) -> str:
        return "read_l4"

    @property
    def taskKey(self) -> str:
        return "workflow_time"

    @property
    def l4_blob_source(self) -> str:
        return self.config["l4_blob_source"]

    @property
    def delta_location(self) -> str:
        return self.config["delta_location"]

    @property
    def delta_schema(self) -> str:
        return self.config["delta_schema"]

    @property
    def ims_delta_schema(self) -> str:
        return self.config["ims_delta_schema"]

    @property
    def save_path(self) -> str:
        return self.config["save_path"]

    @property
    def dynamic_query_blob(self) -> str:
        return self.config["dynamic_query_blob"]

    @property
    def dynamic_query_save_path(self) -> str:
        return self.config["dynamic_query_save_path"]

    @property
    def is_save(self) -> str:
        return self.config["is_save"]

    @property
    def is_workflow_save(self) -> str:
        return self.config["is_workflow_save"]

    @property
    def g_all_thryld_mm_byplatform(self) -> str:
        return self.idashboard_cloud_tablename["g_all_thryld_mm_byplatform"]

    @property
    def g_all_thryld_mm_bymodel(self) -> str:
        return self.idashboard_cloud_tablename["g_all_thryld_mm_bymodel"]

    @property
    def s_all_thryld_monthly_byplatform(self) -> str:
        return self.idashboard_cloud_tablename["s_all_thryld_monthly_byplatform"]

    @property
    def s_all_thryld_monthly_byplatformfab(self) -> str:
        return self.idashboard_cloud_tablename["s_all_thryld_monthly_byplatformfab"]

    @property
    def s_all_thryld_mtd_byplatform(self) -> str:
        return self.idashboard_cloud_tablename["s_all_thryld_mtd_byplatform"]

    @property
    def s_all_thryld_mtd_byplatformfab(self) -> str:
        return self.idashboard_cloud_tablename["s_all_thryld_mtd_byplatformfab"]

    @property
    def idashboard_10_oracle_connection(self) -> str:
        return f"{self.idashboard_onpremise['user']}/{self.idashboard_onpremise['password']}@{self.idashboard_onpremise['host']}:{self.idashboard_onpremise['port']}"

    @property
    def idashboard_10_schema(self) -> str:
        return f"{self.idashboard_onpremise['db_schema']}"

    @property
    def idashboard_10_tablename(self) -> str:
        return f"{self.idashboard_onpremise['tablename']}"

    @property
    def stage(self) -> str:
        return ["ARRAY", "FEOL", "ARRAY_OTP", "CELL_OTP", "CELL",
                "JI", "MODULE_SFG_OTP", "MODULE_SFG", "MODULE_OTP", "MODULE", "MODULE_92_FULL"]

    @property
    def pk_summary(self) -> str:
        pk_summary_dict = {
            "byplatformsite": ["IE_BU", "PLATFORM", "SITE", "REMAIN_FLAG", "MFG_PERIOD", "PERIOD_TYPE"],
            "byplatform": ["IE_BU", "PLATFORM", "REMAIN_FLAG", "MFG_PERIOD", "PERIOD_TYPE"],
            "byplatformfab": ["IE_BU", "PLATFORM", "A_SITE", "REMAIN_FLAG", "MFG_PERIOD", "PERIOD_TYPE"],
            "byproduct_summary": ["IE_BU", "PLATFORM", "REMAIN_FLAG", "MODULE_PRODUCT_CODE", "A_SITE", "MFG_PERIOD", "PERIOD_TYPE"],
            "byproduct_version_summary": ["IE_BU", "PLATFORM", "REMAIN_FLAG", "PRODUCT_CODE_VERSION", "A_SITE", "MFG_PERIOD", "PERIOD_TYPE"],
            "byproduct_extend_summary": ["IE_BU", "PLATFORM", "REMAIN_FLAG", "PRODUCT_CODE_EXTEND", "A_SITE", "MFG_PERIOD", "PERIOD_TYPE"],
            "byproduct_detail": ["IE_BU", "PLATFORM", "REMAIN_FLAG", "MODULE_PRODUCT_CODE", "PARENT_PRODUCT_CODE", "CAR_ASM_SUB_PRODUCT_CODE", "GROUPBY_PRODUCT_CODE", "MFG_PERIOD", "PERIOD_TYPE", "GROUPBY_A_SITE"],
            "byproduct_version_detail": ["IE_BU", "PLATFORM", "REMAIN_FLAG", "PRODUCT_CODE_VERSION", "PARENT_PRODUCT_CODE_VERSION", "CAR_ASM_SUB_PRODUCT_CODE", "GROUPBY_PRODUCT_CODE_VERSION", "MFG_PERIOD", "PERIOD_TYPE", "GROUPBY_A_SITE"],
            "byproduct_extend_detail": ["IE_BU", "PLATFORM", "REMAIN_FLAG", "PRODUCT_CODE_EXTEND", "PARENT_PRODUCT_CODE_EXTEND", "CAR_ASM_SUB_PRODUCT_CODE", "GROUPBY_PRODUCT_CODE_EXTEND", "MFG_PERIOD", "PERIOD_TYPE", "GROUPBY_A_SITE"],
            "byfab": ["A_SITE", "MFG_PERIOD", "REMAIN_FLAG", "PERIOD_TYPE"],
        }

        if self.is_web:
            pk_summary_web_dict = {}
            pk_summary_web_dict["byplatform"] = pk_summary_dict["byplatform"]
            pk_summary_web_dict[self.web_detail_groupby] = pk_summary_dict[self.web_detail_groupby]
            return pk_summary_web_dict
        else:
            return pk_summary_dict

    @property
    def module_pk_summary(self) -> str:
        module_pk_summary = {
            "byplatformsite": ["IE_BU", "PLATFORM", "SITE", "REMAIN_FLAG", "YIELD_TYPE", "MFG_PERIOD", "PERIOD_TYPE"],
            "byplatform": ["IE_BU", "PLATFORM", "REMAIN_FLAG", "YIELD_TYPE", "MFG_PERIOD", "PERIOD_TYPE"],
            "byplatformfab": ["IE_BU", "PLATFORM", "REMAIN_FLAG", "YIELD_TYPE", "A_SITE", "MFG_PERIOD", "PERIOD_TYPE"],
            "byproduct_summary": ["IE_BU", "PLATFORM", "REMAIN_FLAG", "YIELD_TYPE", "MODULE_PRODUCT_CODE", "A_SITE", "MFG_PERIOD", "PERIOD_TYPE"],
            "byproduct_version_summary": ["IE_BU", "PLATFORM", "REMAIN_FLAG", "YIELD_TYPE", "PRODUCT_CODE_VERSION", "A_SITE", "MFG_PERIOD", "PERIOD_TYPE"],
            "byproduct_extend_summary": ["IE_BU", "PLATFORM", "REMAIN_FLAG", "YIELD_TYPE", "PRODUCT_CODE_EXTEND", "A_SITE", "MFG_PERIOD", "PERIOD_TYPE"],
            "byproduct_detail": ["IE_BU", "PLATFORM", "REMAIN_FLAG", "MODULE_PRODUCT_CODE", "PARENT_PRODUCT_CODE", "CAR_ASM_SUB_PRODUCT_CODE", "GROUPBY_PRODUCT_CODE", "MFG_PERIOD", "PERIOD_TYPE",
                                 "A_SITE", "GROUPBY_A_SITE", "F_SITE", "OTP_A_SITE", "OTP_C_SITE", "NFG_C_SITE", "C_SITE", "J_SITE", "OTP_SFG_M_SITE", "SFG_M_SITE", "OTP_M_SITE", "M_SITE",
                                 "PHASE", "LEVEL", "CELL_LEVEL", "CHIP_TYPE", "WO_TYPE"],
            "byproduct_version_detail": ["IE_BU", "PLATFORM", "REMAIN_FLAG", "PRODUCT_CODE_VERSION", "PARENT_PRODUCT_CODE_VERSION", "CAR_ASM_SUB_PRODUCT_CODE", "GROUPBY_PRODUCT_CODE_VERSION", "MFG_PERIOD", "PERIOD_TYPE",
                                         "A_SITE", "GROUPBY_A_SITE", "F_SITE", "OTP_A_SITE", "OTP_C_SITE", "NFG_C_SITE", "C_SITE", "J_SITE", "OTP_SFG_M_SITE", "SFG_M_SITE", "OTP_M_SITE", "M_SITE",
                                         "PHASE", "LEVEL", "CELL_LEVEL", "CHIP_TYPE", "WO_TYPE"],
            "byproduct_extend_detail": ["IE_BU", "PLATFORM", "REMAIN_FLAG", "PRODUCT_CODE_EXTEND", "PARENT_PRODUCT_CODE_EXTEND", "CAR_ASM_SUB_PRODUCT_CODE", "GROUPBY_PRODUCT_CODE_EXTEND", "MFG_PERIOD", "PERIOD_TYPE",
                                        "A_SITE", "GROUPBY_A_SITE", "F_SITE", "OTP_A_SITE", "OTP_C_SITE", "NFG_C_SITE", "C_SITE", "J_SITE", "OTP_SFG_M_SITE", "SFG_M_SITE", "OTP_M_SITE", "M_SITE",
                                        "PHASE", "LEVEL", "CELL_LEVEL", "CHIP_TYPE", "WO_TYPE"],
            "byfab": ["A_SITE", "REMAIN_FLAG", "YIELD_TYPE", "MFG_PERIOD", "PERIOD_TYPE"],
        }

        if self.is_web:
            module_pk_summary_web_dict = {}
            module_pk_summary_web_dict["byplatform"] = module_pk_summary["byplatform"]
            module_pk_summary_web_dict[self.web_detail_groupby] = module_pk_summary[self.web_detail_groupby]
            return module_pk_summary_web_dict
        else:
            return module_pk_summary

    @property
    def c_stage_path_qty_mapping(self) -> str:
        return "c_stage_path_qty_mapping"

    @property
    def mf_all_s_all_yld_at_l4_bypart_qtys(self) -> str:
        return "mf_all_s_all_yld_at_l4_bypart_qtys"

    @property
    def c_partno_productCodeVer_productCode_BU(self) -> str:
        return "c_partno_productCodeVer_productCode_BU"

    @property
    def c_partno_productCodeVer_productCode_BU_parent_partno(self) -> str:
        return "c_partno_productCodeVer_productCode_BU_parent_partno"

    @property
    def c_fab_site(self) -> str:
        return "c_fab_site"

    @property
    def c_car2in1_product_mapping(self) -> str:
        return "c_car2in1_product_mapping"

    @property
    def mf_all_s_all_yld_at_L4_plot_dim(self) -> str:
        return "mf_all_s_all_yld_at_L4_plot_dim"

    @property
    def c_l4_module_stage_bypart_mapping(self) -> str:
        return "c_l4_module_stage_bypart_mapping"

    @property
    def c_ie_platform_condition(self) -> str:
        return "c_ie_platform_condition"

    @property
    def c_ie_partno_platform(self) -> str:
        return "c_ie_partno_platform"

    @property
    def mf_all_g_all_yld_at_c_byplatform_year_target(self) -> str:
        return "mf_all_g_all_yld_at_c_byplatform_year_target"

    @property
    def mf_all_g_all_yld_at_c_byproduct_commit_yld(self) -> str:
        return "mf_all_g_all_yld_at_c_byproduct_commit_yld"

    @property
    def mf_all_s_all_yld_at_L4_array_part(self) -> str:
        return "mf_all_s_all_yld_at_L4_array_part"

    @property
    def mf_all_s_all_yld_at_L4_cell_part(self) -> str:
        return "mf_all_s_all_yld_at_L4_cell_part"

    @property
    def mf_all_s_all_yld_at_L4_ji_part(self) -> str:
        return "mf_all_s_all_yld_at_L4_ji_part"

    @property
    def mf_all_s_all_yld_at_L4_ma_part(self) -> str:
        return "mf_all_s_all_yld_at_L4_ma_part"

    @property
    def mf_all_s_all_yld_at_L4_sfg_part(self) -> str:
        return "mf_all_s_all_yld_at_L4_sfg_part"

    @property
    def mf_all_s_array_yld_at_l5_tracing_byproduct(self) -> str:
        return "mf_all_s_array_yld_at_l5_tracing_byproduct"

    @property
    def mf_all_s_array_otp_yld_at_l5_tracing_byproduct(self) -> str:
        return "mf_all_s_array_otp_yld_at_l5_tracing_byproduct"

    @property
    def mf_all_s_cell_yld_at_L5_tracing_byproduct(self) -> str:
        return "mf_all_s_cell_yld_at_L5_tracing_byproduct"

    @property
    def mf_all_s_cell_otp_yld_at_l5_tracing_byproduct(self) -> str:
        return "mf_all_s_cell_otp_yld_at_l5_tracing_byproduct"

    @property
    def mf_all_s_all_yld_at_L5_array_byproduct_detail(self) -> str:
        return "mf_all_s_all_yld_at_L5_array_byproduct_detail"

    @property
    def mf_all_s_all_yld_at_L5_cell_byproduct_detail(self) -> str:
        return "mf_all_s_all_yld_at_L5_cell_byproduct_detail"

    @property
    def mf_all_s_all_yld_at_L5_ji_byproduct_detail(self) -> str:
        return "mf_all_s_all_yld_at_L5_ji_byproduct_detail"

    @property
    def mf_all_s_all_yld_at_L5_ma_byproduct_detail(self) -> str:
        return "mf_all_s_all_yld_at_L5_ma_byproduct_detail"

    @property
    def mf_all_s_all_yld_at_L5_sfg_byproduct_detail(self) -> str:
        return "mf_all_s_all_yld_at_L5_sfg_byproduct_detail"

    @property
    def mf_all_g_all_yld_at_L6_byproduct_detail(self) -> str:
        return "mf_all_g_all_yld_at_L6_byproduct_detail"

    @property
    def mf_all_s_all_yld_at_L42_array_bypart_with_partno(self) -> str:
        return "mf_all_s_all_yld_at_L42_array_bypart_with_partno"

    @property
    def mf_all_s_all_yld_at_L42_array_bypart_with_partno_platform(self) -> str:
        return "mf_all_s_all_yld_at_L42_array_bypart_with_partno_platform"

    @property
    def mf_all_s_array_otp_yld_at_l42_bypart_with_partno(self) -> str:
        return "mf_all_s_array_otp_yld_at_l42_bypart_with_partno"

    @property
    def mf_all_s_array_otp_yld_at_l42_bypart_with_partno_platform(self) -> str:
        return "mf_all_s_array_otp_yld_at_l42_bypart_with_partno_platform"

    @property
    def mf_all_s_all_yld_at_L42_cell_bypart_with_partno(self) -> str:
        return "mf_all_s_all_yld_at_L42_cell_bypart_with_partno"

    @property
    def mf_all_s_all_yld_at_L42_cell_bypart_with_partno_platform(self) -> str:
        return "mf_all_s_all_yld_at_L42_cell_bypart_with_partno_platform"

    @property
    def mf_all_s_cell_otp_yld_at_l42_bypart_with_partno(self) -> str:
        return "mf_all_s_cell_otp_yld_at_l42_bypart_with_partno"

    @property
    def mf_all_s_cell_otp_yld_at_l42_bypart_with_partno_platform(self) -> str:
        return "mf_all_s_cell_otp_yld_at_l42_bypart_with_partno_platform"

    @property
    def mf_all_s_all_yld_at_L42_ji_bypart_with_partno(self) -> str:
        return "mf_all_s_all_yld_at_L42_ji_bypart_with_partno"

    @property
    def mf_all_s_all_yld_at_L42_ji_bypart_with_partno_platform(self) -> str:
        return "mf_all_s_all_yld_at_L42_ji_bypart_with_partno_platform"

    @property
    def mf_all_s_moudle_otp_yld_at_l42_bypart_with_partno(self) -> str:
        return "mf_all_s_moudle_otp_yld_at_l42_bypart_with_partno"

    @property
    def mf_all_s_moudle_otp_yld_at_l42_bypart_with_partno_platform(self) -> str:
        return "mf_all_s_moudle_otp_yld_at_l42_bypart_with_partno_platform"

    @property
    def mf_all_s_all_yld_at_L42_ma_bypart_with_model(self) -> str:
        return "mf_all_s_all_yld_at_L42_ma_bypart_with_model"

    @property
    def mf_all_s_all_yld_at_L42_ma_bypart_with_model_platform(self) -> str:
        return "mf_all_s_all_yld_at_L42_ma_bypart_with_model_platform"

    @property
    def mf_all_s_all_yld_at_L42_ma_sfg_bypart_with_partno(self) -> str:
        return "mf_all_s_all_yld_at_L42_ma_sfg_bypart_with_partno"

    @property
    def mf_all_s_all_yld_at_L42_ma_sfg_bypart_with_partno_platform(self) -> str:
        return "mf_all_s_all_yld_at_L42_ma_sfg_bypart_with_partno_platform"

    @property
    def mf_all_s_moudle_sfg_otp_yld_at_l42_bypart_with_partno(self) -> str:
        return "mf_all_s_moudle_sfg_otp_yld_at_l42_bypart_with_partno"

    @property
    def mf_all_s_moudle_sfg_otp_yld_at_l42_bypart_with_partno_platform(self) -> str:
        return "mf_all_s_moudle_sfg_otp_yld_at_l42_bypart_with_partno_platform"

    @property
    def mf_all_s_all_yld_at_L5_array_byproduct_summary(self) -> str:
        return "mf_all_s_all_yld_at_L5_array_byproduct_summary"

    @property
    def mf_all_s_all_yld_at_L5_cell_byproduct_summary(self) -> str:
        return "mf_all_s_all_yld_at_L5_cell_byproduct_summary"

    @property
    def mf_all_s_all_yld_at_L5_ji_byproduct_summary(self) -> str:
        return "mf_all_s_all_yld_at_L5_ji_byproduct_summary"

    @property
    def mf_all_s_all_yld_at_L5_sfg_byproduct_summary(self) -> str:
        return "mf_all_s_all_yld_at_L5_sfg_byproduct_summary"

    @property
    def mf_all_s_all_yld_at_L5_ma_byproduct_summary(self) -> str:
        return "mf_all_s_all_yld_at_L5_ma_byproduct_summary"

    @property
    def L53_ma_type_byproduct_summary(self) -> str:
        return "L53_ma_type_byproduct_summary"

    @property
    def mf_all_g_all_yld_at_L6_byproduct_summary(self) -> str:
        return "mf_all_g_all_yld_at_L6_byproduct_summary"

    @property
    def mf_all_s_all_yld_at_L5_array_byfab(self) -> str:
        return "mf_all_s_all_yld_at_L5_array_byfab"

    @property
    def mf_all_s_all_yld_at_L5_cell_byfab(self) -> str:
        return "mf_all_s_all_yld_at_L5_cell_byfab"

    @property
    def mf_all_s_all_yld_at_L5_ji_byfab(self) -> str:
        return "mf_all_s_all_yld_at_L5_ji_byfab"

    @property
    def mf_all_s_all_yld_at_L5_sfg_byfab(self) -> str:
        return "mf_all_s_all_yld_at_L5_sfg_byfab"

    @property
    def mf_all_s_all_yld_at_L5_ma_byfab(self) -> str:
        return "mf_all_s_all_yld_at_L5_ma_byfab"

    @property
    def L53_ma_type_byfab_summary(self) -> str:
        return "L53_ma_type_byfab_summary"

    @property
    def mf_all_g_all_yld_at_L6_byfab(self) -> str:
        return "mf_all_g_all_yld_at_L6_byfab"

    @property
    def mf_all_s_all_yld_at_L5_array_bybuplatform(self) -> str:
        return "mf_all_s_all_yld_at_L5_array_bybuplatform"

    @property
    def mf_all_s_all_yld_at_L5_cell_bybuplatform(self) -> str:
        return "mf_all_s_all_yld_at_L5_cell_bybuplatform"

    @property
    def mf_all_s_all_yld_at_L5_ji_bybuplatform(self) -> str:
        return "mf_all_s_all_yld_at_L5_ji_bybuplatform"

    @property
    def mf_all_s_all_yld_at_L5_sfg_bybuplatform(self) -> str:
        return "mf_all_s_all_yld_at_L5_sfg_bybuplatform"

    @property
    def mf_all_s_all_yld_at_L5_ma_bybuplatform(self) -> str:
        return "mf_all_s_all_yld_at_L5_ma_bybuplatform"

    @property
    def L53_ma_type_bybuplatform_summary(self) -> str:
        return "L53_ma_type_bybuplatform_summary"

    @property
    def mf_all_g_all_yld_at_L6_bybuplatform(self) -> str:
        return "mf_all_g_all_yld_at_L6_bybuplatform"

    @property
    def mf_all_s_all_yld_at_L5_array_byplatformfab(self) -> str:
        return "mf_all_s_all_yld_at_L5_array_byplatformfab"

    @property
    def mf_all_s_all_yld_at_L5_cell_byplatformfab(self) -> str:
        return "mf_all_s_all_yld_at_L5_cell_byplatformfab"

    @property
    def mf_all_s_all_yld_at_L5_ji_byplatformfab(self) -> str:
        return "mf_all_s_all_yld_at_L5_ji_byplatformfab"

    @property
    def mf_all_s_all_yld_at_L5_sfg_byplatformfab(self) -> str:
        return "mf_all_s_all_yld_at_L5_sfg_byplatformfab"

    @property
    def mf_all_s_all_yld_at_L5_ma_byplatformfab(self) -> str:
        return "mf_all_s_all_yld_at_L5_ma_byplatformfab"

    @property
    def L53_ma_type_byplatformfab_summary(self) -> str:
        return "L53_ma_type_byplatformfab_summary"

    @property
    def mf_all_g_all_yld_at_L6_byplatformfab(self) -> str:
        return "mf_all_g_all_yld_at_L6_byplatformfab"

    # ==================================================
    # temp table
    @property
    def array_otp_bypart_qtys(self) -> str:
        return "array_otp_bypart_qtys"

    @property
    def array_otp_byproduct_detail(self) -> str:
        return "array_otp_byproduct_detail"

    @property
    def array_bypart_qtys(self) -> str:
        return "array_bypart_qtys"

    @property
    def feol_bypart_qtys(self) -> str:
        return "feol_bypart_qtys"

    @property
    def array_byproduct_detail(self) -> str:
        return "array_byproduct_detail"

    @property
    def cell_bypart_qtys(self) -> str:
        return "cell_bypart_qtys"

    @property
    def cell_byproduct_detail(self) -> str:
        return "cell_byproduct_detail"

    @property
    def cell_otp_bypart_qtys(self) -> str:
        return "cell_otp_bypart_qtys"

    @property
    def cell_otp_byproduct_detail(self) -> str:
        return "cell_otp_byproduct_detail"

    @property
    def ji_bypart_qtys(self) -> str:
        return "ji_bypart_qtys"

    @property
    def ji_byproduct_detail(self) -> str:
        return "ji_byproduct_detail"

    @property
    def module_bypart_qtys(self) -> str:
        return "module_bypart_qtys"

    @property
    def module_byproduct_detail(self) -> str:
        return "module_byproduct_detail"

    @property
    def module_otp_bypart_qtys(self) -> str:
        return "module_otp_bypart_qtys"

    @property
    def module_otp_byproduct_detail(self) -> str:
        return "module_otp_byproduct_detail"

    @property
    def module_sfg_bypart_qtys(self) -> str:
        return "module_sfg_bypart_qtys"

    @property
    def module_sfg_byproduct_detail(self) -> str:
        return "module_sfg_byproduct_detail"

    @property
    def module_sfg_otp_bypart_qtys(self) -> str:
        return "module_sfg_otp_bypart_qtys"

    @property
    def module_sfg_otp_byproduct_detail(self) -> str:
        return "module_sfg_otp_byproduct_detail"

    # =====================l3_l4============================
    # database
    @property
    def l3_l4_delta_schema(self) -> str:
        return "prod_dw"

    # taskvalue
    @property
    def l3_taskName(self) -> str:
        return "l3_l4_set_job_args"

    # select table
    @property
    def dt_all_s_all_dw_at_auodw_c_fac_fab_mst(self) -> str:
        return "dt_all_s_all_dw_at_auodw_c_fac_fab_mst"

    @property
    def dt_all_s_all_dw_at_auodw_c_dw_prod_mst(self) -> str:
        return "dt_all_s_all_dw_at_auodw_c_dw_prod_mst"

    @property
    def dt_all_s_all_dw_at_auoiway_h_log_thinscrap(self) -> str:
        return "dt_all_s_all_dw_at_auoiway_h_log_thinscrap"

    @property
    def dt_all_s_all_dw_at_auodw_c_rpt_platform_mst(self) -> str:
        return "dt_all_s_all_dw_at_auodw_c_rpt_platform_mst"

    @property
    def dt_all_s_all_dw_at_feedback_h_dax_fbk_master_module_ods(self) -> str:
        return "dt_all_s_all_dw_at_feedback_h_dax_fbk_master_module_ods"

    @property
    def dt_all_s_all_dw_at_feedback_h_dax_fbk_test_ods(self) -> str:
        return "dt_all_s_all_dw_at_feedback_h_dax_fbk_test_ods"

    @property
    def dt_all_s_all_dw_at_lcmstg_c_dw_carprodmap_mst(self) -> str:
        return "dt_all_s_all_dw_at_lcmstg_c_dw_carprodmap_mst"

    @property
    def dt_all_s_all_dw_at_lcmstg_h_dw_kpi_ods_patch(self) -> str:
        return "dt_all_s_all_dw_at_lcmstg_h_dw_kpi_ods_patch"

    @property
    def dt_all_s_all_dw_at_auodw_c_dw_dpspn_mst(self) -> str:
        return "dt_all_s_all_dw_at_auodw_c_dw_dpspn_mst"

    @property
    def dt_all_s_all_dw_at_auodw_c_dw_pn_mst(self) -> str:
        return "dt_all_s_all_dw_at_auodw_c_dw_pn_mst"

    @property
    def dt_all_s_all_dw_at_auodw_c_dw_pntech_mst(self) -> str:
        return "dt_all_s_all_dw_at_auodw_c_dw_pntech_mst"

    @property
    def dt_all_s_all_dw_at_lcmstg_c_dw_carprodmap_mst(self) -> str:
        return "dt_all_s_all_dw_at_lcmstg_c_dw_carprodmap_mst"

    @property
    def dt_all_s_all_dw_at_auodw_c_dw_bgbu_mst(self) -> str:
        return "dt_all_s_all_dw_at_auodw_c_dw_bgbu_mst"

    @property
    def dt_all_s_all_dw_at_lcmstg_c_dw_prodmap_mst(self) -> str:
        return "dt_all_s_all_dw_at_lcmstg_c_dw_prodmap_mst"

    @property
    def l4_csv_weekly(self) -> str:
        return "l4_csv_weekly"

    # create table

    @property
    def h_dw_kpi_ods_v(self) -> str:
        return "dt_all_s_all_dw_at_auodw_h_dw_kpi_ods_v"

    @property
    def mf_all_s_array_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_array_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_feol_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_feol_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_feol_yld_at_l3_thinscrap_bypart_qtys(self) -> str:
        return "mf_all_s_feol_yld_at_l3_thinscrap_bypart_qtys"

    @property
    def mf_all_s_array_otp_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_array_otp_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_cell_otp_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_cell_otp_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_cell_otp_fb_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_cell_otp_fb_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_cell_otp_fb_yld_at_l3_detail_qtys(self) -> str:
        return "mf_all_s_cell_otp_fb_yld_at_l3_detail_qtys"

    @property
    def mf_all_s_cell_final_test_fb_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_cell_final_test_fb_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_cell_final_test_fb_yld_at_l3_detail_qtys(self) -> str:
        return "mf_all_s_cell_final_test_fb_yld_at_l3_detail_qtys"

    @property
    def mf_all_s_cell_lcd_big_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_cell_lcd_big_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_cell_lcd_small_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_cell_lcd_small_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_cell_92_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_cell_92_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_cell_lcd_small_big_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_cell_lcd_small_big_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_cell_lcd_second_92_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_cell_lcd_second_92_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_cell_fb_output_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_cell_fb_output_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_cell_fb_scrap_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_cell_fb_scrap_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_cell_fb_big_size_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_cell_fb_big_size_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_cell_fb_yld_at_l3_detail_qtys(self) -> str:
        return "mf_all_s_cell_fb_yld_at_l3_detail_qtys"

    @property
    def mf_all_s_ji_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_ji_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_ji_fb_output_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_ji_fb_output_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_ji_fb_scrap_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_ji_fb_scrap_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_ji_fb_yld_at_l3_detail_qtys(self) -> str:
        return "mf_all_s_ji_fb_yld_at_l3_detail_qtys"

    @property
    def mf_all_s_module_sfg_otp_fb_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_module_sfg_otp_fb_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_module_sfg_otp_fb_yld_at_l3_detail_qtys(self) -> str:
        return "mf_all_s_module_sfg_otp_fb_yld_at_l3_detail_qtys"

    @property
    def mf_all_s_module_sfg_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_module_sfg_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_module_sfg_patch_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_module_sfg_patch_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_module_sfg_fb_output_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_module_sfg_fb_output_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_module_sfg_fb_scrap_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_module_sfg_fb_scrap_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_module_sfg_fb_yld_at_l3_detail_qtys(self) -> str:
        return "mf_all_s_module_sfg_fb_yld_at_l3_detail_qtys"

    @property
    def mf_all_s_module_otp_fb_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_module_otp_fb_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_module_otp_fb_yld_at_l3_detail_qtys(self) -> str:
        return "mf_all_s_module_otp_fb_yld_at_l3_detail_qtys"

    @property
    def mf_all_s_module_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_module_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_module_yld_at_l3_patch_bypart_qtys(self) -> str:
        return "mf_all_s_module_yld_at_l3_patch_bypart_qtys"

    @property
    def mf_all_s_module_yld_at_l3_92_bypart_qtys(self) -> str:
        return "mf_all_s_module_yld_at_l3_92_bypart_qtys"

    @property
    def mf_all_s_module_yld_at_l3_92_2_bypart_qtys(self) -> str:
        return "mf_all_s_module_yld_at_l3_92_2_bypart_qtys"

    @property
    def mf_all_s_module_yld_at_l3_92_3_bypart_qtys(self) -> str:
        return "mf_all_s_module_yld_at_l3_92_3_bypart_qtys"

    @property
    def mf_all_s_module_yld_at_l3_92_left_join_bypart_qtys(self) -> str:
        return "mf_all_s_module_yld_at_l3_92_left_join_bypart_qtys"

    @property
    def mf_all_s_module_fb_ji_91_output_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_module_fb_ji_91_output_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_module_fb_oth_output_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_module_fb_oth_output_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_module_93_97_99_output_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_module_93_97_99_output_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_module_fb_module_scrap_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_module_fb_module_scrap_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_module_fb_4_output_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_module_fb_4_output_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_module_fb_4_scrap_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_module_fb_4_scrap_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_module_fb_ji_scrap_yld_at_l3_bypart_qtys(self) -> str:
        return "mf_all_s_module_fb_ji_scrap_yld_at_l3_bypart_qtys"

    @property
    def mf_all_s_module_fb_yld_at_l3_detail_qtys(self) -> str:
        return "mf_all_s_module_fb_yld_at_l3_detail_qtys"

    @property
    def mf_all_s_array_yld_at_l3_bypart_with_product_qtys(self) -> str:
        return "mf_all_s_array_yld_at_l3_bypart_with_product_qtys"

    @property
    def mf_all_s_feol_yld_at_l3_bypart_with_product_qtys(self) -> str:
        return "mf_all_s_feol_yld_at_l3_bypart_with_product_qtys"

    @property
    def mf_all_s_array_otp_yld_at_l3_bypart_with_product_qtys(self) -> str:
        return "mf_all_s_array_otp_yld_at_l3_bypart_with_product_qtys"

    @property
    def mf_all_s_cell_otp_yld_at_l3_bypart_with_product_qtys(self) -> str:
        return "mf_all_s_cell_otp_yld_at_l3_bypart_with_product_qtys"

    @property
    def mf_all_s_cell_final_test_yld_at_l3_bypart_with_product_qtys(self) -> str:
        return "mf_all_s_cell_final_test_yld_at_l3_bypart_with_product_qtys"

    @property
    def mf_all_s_cell_yld_at_l3_bypart_with_product_qtys(self) -> str:
        return "mf_all_s_cell_yld_at_l3_bypart_with_product_qtys"

    @property
    def mf_all_s_ji_yld_at_l3_bypart_with_product_qtys(self) -> str:
        return "mf_all_s_ji_yld_at_l3_bypart_with_product_qtys"

    @property
    def mf_all_s_module_sfg_otp_yld_at_l3_bypart_with_product_qtys(self) -> str:
        return "mf_all_s_module_sfg_otp_yld_at_l3_bypart_with_product_qtys"

    @property
    def mf_all_s_module_sfg_yld_at_l3_bypart_with_product_qtys(self) -> str:
        return "mf_all_s_module_sfg_yld_at_l3_bypart_with_product_qtys"

    @property
    def mf_all_s_module_otp_yld_at_l3_bypart_with_product_qtys(self) -> str:
        return "mf_all_s_module_otp_yld_at_l3_bypart_with_product_qtys"

    @property
    def mf_all_s_module_yld_at_l3_bypart_with_product_qtys(self) -> str:
        return "mf_all_s_module_yld_at_l3_bypart_with_product_qtys"

