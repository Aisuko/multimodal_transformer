import os
class Config():
    def __init__(self):
        self.basepath = "/workspaces/Multimodal_Transformer/mmtransformer"
        self.data = '/workspaces/Multimodal_Transformer/data-mimic3/in-hospital-mortality/'
        self.timestep = 1.0
        self.normalizer_state = "/workspaces/Multimodal_Transformer/in_hospital_mortality_normalizer_state/ihm_ts1.0.input_str:previous.start_time:zero.normalizer"
        self.imputation = 'previous'
        self.small_part = False
        self.textdata = self.basepath + 'text/'
        self.buffer_size = 100
        self.learning_rate = 2e-5 #5e-6 #
        self.max_len = 128
        self.break_text_at = 300
        self.padding_type = 'Zero'
        self.ihm_path = "/workspaces/Multimodal_Transformer/data-mimic3/in-hospital-mortality/"
        self.textdata_fixed = "/workspaces/Multimodal_Transformer/data-mimic3/root/text_fixed/"
        self.starttime_path = "/workspaces/Multimodal_Transformer/data-mimic3/root/T0/train_starttime.pkl"
        self.maximum_number_events = 150
        self.test_textdata_fixed = "/workspaces/Multimodal_Transformer/data-mimic3/root/test_text_fixed/"
        self.test_starttime_path = "/workspaces/Multimodal_Transformer/data-mimic3/root/T0/test_starttime.pkl"
        self.dropout = 0.9 #keep_prob
