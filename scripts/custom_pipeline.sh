python ../self_instruct/custom_check_machineisempty.py

batch_dir=../data/gpt3_generations/

python ../self_instruct/bootstrap_instructions.py \
    --batch_dir ${batch_dir} \
    --num_instructions_to_generate 10 \
    --seed_tasks_path ../data/seed_tasks.jsonl \
    --engine "text-davinci-003"

batch_dir=../data/gpt3_generations/

python ../self_instruct/custom_identify_clf_or_not.py \
    --batch_dir ${batch_dir} \
    --engine "text-davinci-003" \
    --request_batch_size 5

batch_dir=../data/gpt3_generations/

python ../self_instruct/custom_generate_instances.py \
    --batch_dir ${batch_dir} \
    --input_file machine_generated_instructions.jsonl \
    --output_file machine_generated_instances.jsonl \
    --max_instances_to_gen 5 \
    --engine "text-davinci-003" \
    --request_batch_size 5

batch_dir=../data/gpt3_generations/

python ../self_instruct/custom_prepare_for_finetuning.py \
    --instance_files ${batch_dir}/machine_generated_instances.jsonl \
    --classification_type_files ${batch_dir}/is_clf_or_not_text-davinci-003_template_1.jsonl \
    --output_dir ${batch_dir}/finetuning_data \
    --include_seed_tasks \
    --seed_tasks_path ../data/seed_tasks.jsonl